import re


def ios_xe_version_parser(text):
    ios_xe_version_names = ["gibraltar", "fuji", "everest", "denali", "ios-xe"]
    ios_xe_version_names_regex = "|".join(ios_xe_version_names)

    ios_xe = re.search(ios_xe_version_names_regex, text, flags=re.IGNORECASE)
    if not ios_xe:
        return

    version_regex = r"version\s+(?P<version>[^\s,]+)"
    version_catch = re.search(version_regex, text, flags=re.IGNORECASE)
    if not version_catch:
        return

    version_number = version_catch.groupdict()['version']
    return version_number
