#!/usr/bin/env python
import MailFormatter
import MailSender
from ProperyLoader import EmailConnection


def send(emailDetails):
    try:
        destination = emailDetails.destination
        subject = emailDetails.subject
        body = MailFormatter.prepare_html_body(emailDetails.href, emailDetails.project_name,
                                               emailDetails.dependency_versions_problem,
                                               emailDetails.dependency_licenses_problem)
        attachment = MailFormatter.prepare_txt_attachement(emailDetails.href, emailDetails.project_name,
                                                           emailDetails.dependency_versions_problem,
                                                           emailDetails.dependency_licenses_problem)
        ec = EmailConnection()
        gm = MailSender.Email(ec)
        attachements = gm.load_attachements(attachment=attachment, attachment_file_name='Message.txt')
        session = gm.init_connection()
        gm.send_message(session, destination, subject, body, attachements)
        gm.close_connection(session)
    except Exception, e:
        print str(e)


class EmailDetails:
    def __init__(self, destination, subject, href, project_name, dependency_versions_problem,
                 dependency_licenses_problem):
        self.destination = destination
        self.subject = subject
        self.href = href
        self.project_name = project_name
        self.dependency_versions_problem = dependency_versions_problem
        self.dependency_licenses_problem = dependency_licenses_problem

emailDetails = EmailDetails('cararuseugeniu@gmail.com', 'VersionEye periodic ntification', 'https://www.versioneye.com/user/projects/56f01b9b35630e003e0a7e4e?child=summary', 'ecararus/product-catalogue ','1 / 24','0 : 0')
send(emailDetails)