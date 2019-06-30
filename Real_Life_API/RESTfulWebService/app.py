from flask import Flask, render_template
from flask import jsonify
from flask import request

app = Flask(__name__)

empDB=[
    {
    'id':'003',
    'name':'Fahim',
    'title':'Assistant Software Engineer'
    },
    {
    'id':'005',
    'name':'Fahim05',
    'title':'Assistant Software Engineer'
    },
    {
    'id':'002',
    'name':'Abdul Kaium',
    'title':'Assistant Software Engineer'
    },
    {
    'id':'101',
    'name':'Saravanan S',
    'title':'Technical Leader'
    },
    {
    'id':'201',
    'name':'Rajkumar P',
    'title':'Sr Software Engineer'
    },
    {
    'id':'102',
    'name':'Shifullah',
    'title':'Trainee Software Engineer'
    }
]

@app.route("/")
def hello():
    # return "Hello World !"
    return render_template("index.html")

@app.route('/empdb/employee/',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})

@app.route('/empdb/employee/employee_id=<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ]
    print("Selected User is: ")
    print(usr)
    return jsonify({'emp':usr})

########################################################################
#PUT method#
########################################################################
# @app.route('/empdb/employee/<empId>',methods=['PUT']) #employee_id=
# def updateEmp(empId):
#     em = [ emp for emp in empDB if (emp['id'] == empId) ]
#     if 'name' in request.json :
#         em[0]['name'] = request.json['name']
#     if 'title' in request.json:
#         em[0]['title'] = request.json['title']
#     return jsonify({'emp':em[0]})

# @app.route('/empdb/employee',methods=['POST'])
# def createEmp():
#     dat = {
#     'id':request.json['id'],
#     'name':request.json['name'],
#     'title':request.json['title']
#     }
#     empDB.append(dat)
#     return jsonify(dat)

##################################################################################
@app.route('/empdb/employee/createNewEmployee/employee_id=<empId>&employee_name=<empName>&employee_designation=<empDesignation>',methods=['GET', 'POST'])  #, 'POST' #'GET',  #&employee_name=<empName>&employee_designation=<empDesignation>
def createNewEmployee(empId, empName, empDesignation): #, empName, empDesignation

    emp_id = empId
    emp_name = empName
    emp_designation = empDesignation
    print("emp_id: "+emp_id)
    print("emp_name: "+emp_name)
    print("emp_designation: "+emp_designation)
    dat = {
        'id':emp_id,
        'name':emp_name,
        'title':emp_designation
    }
    empDB.append(dat)
    return render_template("createEmp.html")
###################################################################################

# @app.route('/empdb/employee/createNewEmployee',methods=['GET' , 'POST'])
# def createNewEmployee():
#     if request.method=="POST":
#         emp_id = request.form["myId"]
#         emp_name = request.form["myName"]
#         emp_designation = request.form["myDesignation"]
#         print("emp_id: "+emp_id)
#         print("emp_name: "+emp_name)
#         print("emp_designation: "+emp_designation)
#         dat = {
#             'id':emp_id,
#             'name':emp_name,
#             'title':emp_designation
#         }
#         empDB.append(dat)
#     return render_template("createEmp.html")

######################################################################
######DELETE method###
#######################################################################
# @app.route('/empdb/employee/<empId>',methods=['DELETE'])
# def deleteEmp(empId):
#     em = [ emp for emp in empDB if (emp['id'] == empId) ]
#     if len(em) == 0:
#         abort(404)
#     empDB.remove(em[0])
#     return jsonify({'response':'Success'})


if __name__ == '__main__':
    app.debug=True
    app.run()
