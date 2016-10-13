#!/usr/bin/env python
from jinja2 import Environment, PackageLoader

def prepare_html_body(href, project_name, dependency_versions_problem, dependency_licenses_problem):
    env = Environment(loader=PackageLoader('mail', '../resources'))
    template = env.get_template('template.html')
    return template.render(href=href, project_name=project_name, dependency_versions_problem=dependency_versions_problem, dependency_licenses_problem=dependency_licenses_problem)

def prepare_txt_attachement(href, project_name, dependency_versions_problem, dependency_licenses_problem):
    env = Environment(loader=PackageLoader('mail', '../resources'))
    template = env.get_template('template.txt')
    return template.render(href=href, project_name=project_name, dependency_versions_problem=dependency_versions_problem, dependency_licenses_problem=dependency_licenses_problem)
