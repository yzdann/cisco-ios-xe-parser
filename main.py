from parser import ios_xe_version_parser
from snmp_data_samples import snmp_samples_list


if __name__ == "__main__":
    for sample in snmp_samples_list:
        version = ios_xe_version_parser(sample)
        print(version)
