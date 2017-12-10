"""
	{
		"createdOn": "10 DEC 2017",
		"updatedOn": "10 DEC 2017"
	}
"""

import appscheck

ac = appscheck.AppsCheck();
if ac.ok:
    appscheck.AppsCheck.check_apps_status()