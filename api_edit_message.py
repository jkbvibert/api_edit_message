import requests
import json

headers = {'Content-Type': 'application/json;charset=utf-8','<session_key_header>': '<scrubbed>'}

data = {
	"data":{
		"type":"message",
		"subject":"message update 1 #5",
		"body":"This is the updated message body"
		#"content_workflow_action":{
			#"workflow_action":"publish",
			#"is_minor_edit":"true"
			#"is_edit_action":"true"
		}
	}
#}

data2 = {
	"data":{
		"type":"message",
		"subject":"message update 2 #5",
		"body":"This is the updated message body"
		#"content_workflow_action":{
			#"workflow_action":"publish",
			#"is_minor_edit":"true"
			#"is_edit_action":"true"
		}
	}
#}

data3 = {
	"data":{
		"type":"message",
		"subject":"message update 3 #5",
		"body":"This is the updated message body"
		#"content_workflow_action":{
			#"workflow_action":"publish",
			#"is_minor_edit":"true"
			#"is_edit_action":"true"
		}
	}
#}


r = requests.put(url = "<hostname>/api/2.0/messages/899", data = json.dumps(data, default=str), headers=headers)
r2 = requests.put(url = "<hostname>/api/2.0/messages/896", data = json.dumps(data2, default=str), headers=headers)
r3 = requests.put(url = "<hostname>/api/2.0/messages/866", data = json.dumps(data3, default=str), headers=headers)
r_formatted = r.json()
r2_formatted = r2.json()
r3_formatted = r3.json()
print(r_formatted)
print(r2_formatted)
print(r3_formatted)