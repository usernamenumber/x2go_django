import json
from django.shortcuts import render
from forms import UserForm
from util import shadowcrypt

def index(request):
    user_fields = [ "username","password","first_name","last_name","email" ]
    c = {"welcome_msg":"WELCOME!"}
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
	    user_data = {}
	    for f in user_fields:
	        user_data[f] = new_user.serializable_value(f)
            if user_data.has_key("password"):
               user_data["password"] = shadowcrypt(user_data["password"])   
	    print "<pre>%s</pre>" % user_data
            open("/usr/local/tunapanda/data/handoff/state/users/%s.json" % user_data["username"],"w").write(json.dumps(user_data))
            c['new_user'] = new_user
        else:
            c['error'] = True
    else:
        form = UserForm()
    c['form'] = form
    return render(request,'tunapanda/index.html',c)


