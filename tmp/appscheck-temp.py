"""
    {
        "createdOn": "07 Dec 2017",
        "updatedOn": "10 Dec 2017",
        "aim": "To check the status of apps",
        "dependecies": "Python's requests module",
        "howWillItWork": "It will create 1 html file regarding the apps status and open it in your Ubuntu M/C"
    }
"""

import os
import subprocess
import requests
import json


class AppsCheck(object):
    file_read = False
    config = None
    ok = False

    def __init__(self):
        if not AppsCheck.file_read:
            AppsCheck.read_config()
        AppsCheck.ok = True

    @staticmethod
    def read_config():
        try:
            with open("config.json") as config_file:
                AppsCheck.config = json.load(config_file)

            AppsCheck.ok = True
            AppsCheck.file_read = True
        except Exception as e:
            print "Error: ", e
            AppsCheck.ok = False

    @staticmethod
    def check_apps_status():
        try:
            if AppsCheck.config:
                """ ******************** Checking for APIS *********************************************** """
                print "\n*********************************APIS*********************************************\n"
                print "|%s|" % ("-" * 80)
                count = 0
                s = "STATUS CODE => "
                style = """<style>
                            #apps {
                                font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                                border-collapse: collapse;
                                width: 100%;
                            }

                            #apps td, #apps th {
                                border: 1px solid #ddd;
                                padding: 8px;
                                color: white;
                            }

                            #apps tr:hover {background-color: pink;}

                            #apps th {
                                padding-top: 12px;
                                padding-bottom: 12px;
                                text-align: left;
                                background-color: black;
                                color: white;
                            }
                            body {
                                padding-top: 0px;
                                padding-left: 200px;
                                padding-right: 200px;
                                border: 0px;
                                background-color: gray;
                            }
                            #head-title{
                                color: white;
                                font-weight:bold;
                                padding: 10px;
                                border: 1px solid lightgreen;
                            }
                            img{
                                width: 32px;
                                height: 32px;
                                border: 0px;
                                padding: 0px;
                            }
                            </style>
                    """

                htmlText = "<!DOCTYPE html>"
                htmlText += "<head lang='en-US'><title>Application Status (" + \
                    AppsCheck.config["environment"] + ")</title>"
                htmlText += style
                htmlText += "</head><body>"
                htmlText += "<center><h1 id='head-title'><img alt='App' src='https://cdn2.iconfinder.com/data/icons/social-media-icons-23/800/tinder-512.png'> Application Status (" + \
                    AppsCheck.config["environment"] + ")</h1></center><br>"
                htmlText += "<table id='apps'><tr><th>Service</th>"
                htmlText += "<th>Status</th></tr>"

                for app in AppsCheck.config["api"]:
                    if app == "environment":  # "environment is not a dictionary so continue with next iteration"
                        continue

                    print app

                    try:
                        count += 1
                        url = AppsCheck.config["api"][app]["url"]
                        print "|%-80s|" % ("(" + str(count) + ") Hitting =>" + str(url))
                        response = requests.get(url)
                        status = str(response.status_code)
                        s += status

                        if status == "200":
                            print "|%-80s|" % ("UP, " + s)
                            htmlText += "<tr style='background-color:#4CAF50'><td>" + app + "</td>"
                            htmlText += "<td>UP</td></tr>"
                        else:
                            print "|%-80s|" % ("DOWN, " + s)
                            htmlText += "<tr style='background-color:#FA8072'><td>" + app + "</td>"
                            htmlText += "<td>DOWN</td></tr>"
                    except requests.exceptions.ConnectionError:
                        print "|%-80s|" % ("DOWN")
                        htmlText += "<tr style='background-color:#FA8072'><td>" + app + "</td>"
                        htmlText += "<td>DOWN</td></tr>"
                    print "|%s|" % ("-" * 80)

                """ ******************** Checking for SERVICES ******************************************* """
                print "\n**********************************SERVICES******************************************"
                count = 0
                for app in AppsCheck.config["service"]:
                    try:
                        count += 1
                        url = AppsCheck.config["service"][app]["cmd"]
                        print "|%-80s|" % ("(" + str(count) + ") Hitting =>" + str(url))
                        exit_code = subprocess.Popen(
                            ['service', app, 'status']).wait()
                        print "exit_code", exit_code

                        if exit_code == 0:
                            print "|%-80s|" % ("UP, " + s)
                            htmlText += "<tr style='background-color:#4CAF50'><td>" + app + "</td>"
                            htmlText += "<td>UP</td></tr>"
                        else:
                            print "|%-80s|" % ("DOWN, " + s)
                            htmlText += "<tr style='background-color:#FA8072'><td>" + app + "</td>"
                            htmlText += "<td>DOWN</td></tr>"
                    except Exception:
                        print "|%-80s|" % ("DOWN")
                        htmlText += "<tr style='background-color:#FA8072'><td>" + app + "</td>"
                        htmlText += "<td>DOWN</td></tr>"
                    print "|%s|" % ("-" * 80)

                htmlText += "</table></body></html>"

                # Creating HTML if it does not exist else overwrite the content
                with open("app_status.html", "w") as app_status_file:
                    app_status_file.write(htmlText)

                print "Opening HTML"
                # 'xdg-open app_status.html' is for UNIX/LINUX & 'open app_status.html' is for MAC
                os.system(AppsCheck.config["commandToOpenTemplate"])
            else:
                print "Config is empty"
        except Exception as err:
            print "Error: ", err


# Starting point of application
if __name__ == "__main__":
    ac = AppsCheck()
    if ac.ok:
        AppsCheck.check_apps_status()





