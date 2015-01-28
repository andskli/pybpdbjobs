JOB_TYPE = {
    0: 'Backup', 1: 'Archive', 2: 'Restore', 3: 'Verify', 4: 'Duplication',
    5: 'Import', 6: 'DB Backup', 7: 'Vault',
}

JOB_STATE = {
    0: 'Queued', 1: 'Active', 2: 'Re-Queued', 3: 'Done',
}

SCHEDULE_TYPE = {
    0: 'Full', 1: 'Differential', 2: 'User Backup', 3: 'User Archive',
    4: 'Cumulative',
}

SUB_TYPE = {
    0: 'Immediate', 1: 'Scheduled', 2: 'User-Initiated',
}

RETENTION_UNITS = {
    0: 'Unknown', 1: 'Days', 2: 'Unknown',
}

POLICY_TYPE = {
    0: 'Standard', 1: 'Proxy', 2: 'Non-Standard', 3: 'Apollo-wbak',
    4: 'Oracle',
    5: 'Any policy type', 6: 'Informix-On-BAR', 7: 'Sybase',
    8: 'MS-Sharepoint', 9: 'UNSPEC', 10: 'NetWare',
    11: 'DataTools-SQL-BackTrack', 12: 'Auspex-FastBackup',
    13: 'MS-Windows-NT', 14: 'OS/2', 15: 'MS-SQL-Server',
    16: 'MS-Exchange-Server', 17: 'SAP', 18: 'DB2', 19: 'NDMP',
    20: 'FlashBackup', 21: 'Split-Mirror', 22: 'AFS', 23: 'UNSPEC',
    24: 'DataStore', 25: 'Lotus-Notes', 26: 'UNSPEC', 27: 'UNSPEC',
    28: 'MPE/iX', 29: 'FlashBackup-Windows', 30: 'Vault',
    31: 'BE-MS-SQL-Server', 32: 'BE-MS-Exchange-Server', 33: 'UNSPEC',
    34: 'Disk Staging', 35: 'NBU-Catalog',
}