import MySQLdb
from flask import Flask, request, jsonify, session
from flask_mysqldb import MySQL
from werkzeug.routing import ValidationError

app = Flask(__name__)
app.config['MYSQL_HOST'] = '35.213.140.165'
app.config['MYSQL_USER'] = 'uwgwdvoi7jwmp'
app.config['MYSQL_PASSWORD'] = 'Clinicalfirst@123'
app.config['MYSQL_DB'] = 'dbim4u0mfuramq'
mysql = MySQL(app)


################################## PATIENT_PERSONAL_DETAILS ######################################

@app.route('/REG_Patient_Personal', methods=['POST'])
def personal():
    if request.method == 'POST':
        user = request.json
        pat_name = user['PATIENT_NAME']
        pat_phone = user['PATIENT_PHONE_NUMBER']
        alt_phn_number = user['ALTERNATIVE_PHONE_NUMBER']
        email = user['EMAIL_ADDRESS']
        password = user['PASSWORD']
        address = user['ADDRESS']
        dob = user['DOB']
        age = user['AGE']
        gender = user['GENDER']
        marital_status = user['MARITAL_STATUS']
        spouse_name = user['SPOUSE_NAME_IF_MARRIED']
        spouse_phone = user['SPOUSE_PHONE_NUMBER']
        patient_employer = user['PATIENTS_EMPLOYER']
        employ_status = user['EMPLOYMENT_STATUS']
        emp_id = user['EMPLOY_ID']
        body_temp = user['BODY_TEMPERATURE']
        blood_pressure = user['BLOOD_PRESSURE']
        ht = user['HEIGHT']
        wt = user['WEIGHT']
        diabetes = user['DIABETES']
        blood_group = user['BLOOD_GROUP']
        transfused = user['TRANSFUSED_IN_LAST_3MONTHS']
        emer_cont_name = user['EMERGENCY_CONTACT_NAME']
        relation_to_patient = user['RELATION_TO_PATIENT']
        emer_cont_address = user['EMERGENCY_CONT_ADDRESS']
        emer_cont_phone = user['EMERGENCY_PHONE_NUMBER']
        cur = mysql.connection.cursor()
        cur.execute('insert into REG_PATIENT_PERSONAL_DETAILS(PATIENT_NAME,PATIENT_PHONE_NUMBER,'
                    'ALTERNATIVE_PHONE_NUMBER,EMAIL_ADDRESS,PASSWORD,ADDRESS,DOB,AGE,GENDER,MARITAL_STATUS,'
                    'SPOUSE_NAME_IF_MARRIED,SPOUSE_PHONE_NUMBER,PATIENTS_EMPLOYER,EMPLOYMENT_STATUS,EMPLOY_ID,'
                    'BODY_TEMPERATURE,BLOOD_PRESSURE,HEIGHT,WEIGHT,DIABETES,BLOOD_GROUP,TRANSFUSED_IN_LAST_3MONTHS,'
                    'EMERGENCY_CONTACT_NAME,RELATION_TO_PATIENT,EMERGENCY_CONT_ADDRESS,EMERGENCY_PHONE_NUMBER) '
                    'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (pat_name, pat_phone, alt_phn_number, email, password, address, dob, age, gender,
                     marital_status, spouse_name, spouse_phone, patient_employer,
                     employ_status, emp_id, body_temp, blood_pressure, ht, wt, diabetes,
                     blood_group, transfused, emer_cont_name, relation_to_patient,
                     emer_cont_address, emer_cont_phone))
        mysql.connection.commit()

        return 'data inserted successfully'


####################### PATIENT_FAMILY_DETAILS ##########################
@app.route('/family_reg', methods=['POST'])
def family():
    if request.method == 'POST':
        PFM_ID = request.json['PFM_ID']
        FAMILY_MEM_NAME = request.json['FAMILY_MEM_NAME']
        RELATION_TO_USER = request.json['RELATION_TO_USER']
        DOB = request.json['DOB']
        GENDER = request.json['GENDER']
        cur = mysql.connection.cursor()
        cur.execute('insert into REG_PATIENT_FAMILY (PFM_ID,FAMILY_MEM_NAME,RELATION_TO_USER,DOB,GENDER)'
                    'VALUES(%s,%s,%s,%s,%s)', (PFM_ID, FAMILY_MEM_NAME, RELATION_TO_USER, DOB, GENDER))

        mysql.connection.commit()
        return "Success"


######################################## DISABILITY #############################################


@app.route('/REG_Disability', methods=['POST'])
def REG_Disability():
    DISABLED_STATUS = request.json['DISABLED_STATUS']
    AVIALABILITY = request.json['AVAILABILITY']

    cur = mysql.connection.cursor()
    cur.execute("select DISABLED_ID from DISABLED_PATIENT where DISABLED_STATUS=%s", (DISABLED_STATUS,))
    dataa = cur.fetchone()

    cur.execute("select CERTIFICATE_ID from DISABILITY_CERTIFICATE where AVAILABILITY=%s", (AVIALABILITY,))
    data = cur.fetchone()

    if "CER001" in data:
        CERTIFICATE_NUMBER = request.json['CERTIFICATE_NUMBER']
        ISSUE_DATE = request.json['ISSUE_DATE']
        DISABILITY_PERCENTAGE = request.json['DISABILITY_PERCENTAGE']
        AUTHORITY_NAME = request.json['AUTHORITY_NAME']
        cur.execute("select AUTHORITY_ID from DISABILITY_ISSUING_AUTHORITY where AUTHORITY_NAME=%s",
                    (AUTHORITY_NAME,))
        data1 = cur.fetchone()

        DISABILITY_TYPE_NAME = request.json['DISABILITY_TYPE_NAME']
        cur.execute("select DISABILITY_TYPE_ID from DISABILITY_TYPE where DISABILITY_TYPE_NAME=%s",
                    (DISABILITY_TYPE_NAME,))
        data2 = cur.fetchone()

        STATUS = request.json['STATUS']
        cur.execute("select DISABILITY_BY_BIRTH_ID from DISABILITY_BY_BIRTH where STATUS=%s", (STATUS,))
        data3 = cur.fetchone()

        if 'DBID001' in data3:
            PENSIONCARD_NUMBER = request.json['PENSIONCARD_NUMBER']
            DISABILITY_AREA_NAME = request.json['DISABILITY_AREA_NAME']
            cur.execute("select DISABILITY_AREA_ID from DISABILITY_AREA where DISABILITY_AREA_NAME=%s",
                        (DISABILITY_AREA_NAME,))
            data4 = cur.fetchone()
            DISABILITY_DUE_NAME = request.json['DISABILITY_DUE_NAME']
            cur.execute("select DISABILITY_DUE_ID from DISABILITY_DUE_TO where DISABILITY_DUE_NAME=%s",
                        (DISABILITY_DUE_NAME,))
            data5 = cur.fetchone()
            DISABILITY_SCHEME = request.json['DISABILITY_SCHEME']
            cur.execute(
                "insert into REG_DISABILITY_DETAILS(DISABLED_ID,CERTIFICATE_ID,CERTIFICATE_NUMBER,ISSUE_DATE,"
                "DISABILITY_PERCENTAGE,DETAILS_OF_ISSUING_AUTHORITY,DISABILITY_TYPE_ID,DISABILITY_BY_BIRTH_ID,"
                "PENSIONCARD_NUMBER,DISABILITY_AREA_ID,DISABILITY_DUE_TO,DISABILITY_SCHEME)"
                " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (dataa, data, CERTIFICATE_NUMBER, ISSUE_DATE,
                                                                 DISABILITY_PERCENTAGE, data1, data2, data3,
                                                                 PENSIONCARD_NUMBER, data4, data5,
                                                                 DISABILITY_SCHEME))
            mysql.connection.commit()
            return "SUCCESS"
        else:
            cur.execute(
                "insert into REG_DISABILITY_DETAILS(DISABLED_ID,CERTIFICATE_ID,CERTIFICATE_NUMBER,ISSUE_DATE,"
                "DISABILITY_PERCENTAGE,DETAILS_OF_ISSUING_AUTHORITY,DISABILITY_TYPE_ID,DISABILITY_BY_BIRTH_ID)"
                " values(%s,%s,%s,%s,%s,%s,%s,%s)", (dataa, data, CERTIFICATE_NUMBER, ISSUE_DATE,
                                                     DISABILITY_PERCENTAGE, data1, data2, data3))
            mysql.connection.commit()
            return 'successfully inserted values'

    cur.execute("insert into REG_DISABILITY_DETAILS(DISABLED_ID,CERTIFICATE_ID)"
                " values(%s,%s)", (dataa, data,))
    mysql.connection.commit()
    return 'successfully inserted values without disability'

    ####################################### ORGAN #################################


@app.route('/REG_Organ', methods=["POST", "GET"])
def Organ_Transplant():
    if request.method == 'POST':
        Procedure_Name = request.json['Procedure_type_name']
        ORGAN = request.json['ORGAN_NAME']
        Complication = request.json['Complication_type_name']
        Med = request.json['Medication']
        Des = request.json['Description']
        cur = mysql.connection.cursor()
        cur.execute("select Procedure_type_ID from REMOVAL_OR_TRANSPLANTATION_OF_ANY_ORGAN "
                    "where Procedure_type_name=%s", (Procedure_Name,))
        abc = cur.fetchone()
        if abc is None:
            return "Please enter correct speciality"
        cur.execute("select ORGAN_ID from ORGANS where ORGAN_NAME=%s", (ORGAN,))
        pqr = cur.fetchone()
        if pqr is None:
            return "please enter correct speciality"
        cur.execute(
            "select Complication_type_ID from ORGAN_COMPLICATIONS_TABLE where Complication_type_name=%s",
            (Complication,))
        xyz = cur.fetchone()
        x = "CRTO001"
        y = "CRTO002"
        if x in xyz:
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute(
                "insert into REG_REMOVAL_OR_TRANSPLANTATION_DETAILS "
                "(Procedure_,ORGAN,Complication,Medication,Description)VALUES(%s,%s,%s,%s,%s)",
                (abc, pqr, xyz, Med, Des))
            mysql.connection.commit()
            cur.close()
        elif y in xyz:
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute(
                "insert into REG_REMOVAL_OR_TRANSPLANTATION_DETAILS (Procedure_,ORGAN,Complication) "
                "VALUES(%s,%s,%s)", (abc, pqr, xyz))
            mysql.connection.commit()
            cur.close()
        mysql.connection.commit()
        cur.close()
        return 'Successfully Inserted'
    else:
        return "Unsuccessful"

        ####################################### INSURANCE ############################################


@app.route('/REG_INSURANCE', methods=['POST'])
def REG_INSURANCE():
    if request.method == 'POST':
        # PATIENT_ID = session['PATIENT_ID']
        Primary_Insurance = request.json['Primary_Insurance']
        Primary_Insured_Name = request.json['Primary_Insured_Name']
        Primary_Policy_ID = request.json['Primary_Policy_ID']
        Secondary_Insurance = request.json['Secondary_Insurance']
        Secondary_Insured_Name = request.json['Secondary_Insured_Name']
        Secondary_Policy_ID = request.json['Secondary_Policy_ID']

        cur = mysql.connection.cursor()
        cur.execute('insert into REG_INSURANCE_DETAILS values(%s,%s,%s,%s,%s,%s)',
                    (Primary_Insurance, Primary_Insured_Name, Primary_Policy_ID, Secondary_Insurance,
                     Secondary_Insured_Name, Secondary_Policy_ID))
        mysql.connection.commit()
        return 'Insurance Details Inserted successful'
    else:
        return " Insurance Details Not Inserted"

        ############################ PREGNANCY DETAILS ###############################


@app.route('/REG_Pregnancy_Details', methods=['POST'])
def Pregnancy_Details():
    if request.method == 'POST':
        u = request.json
        pregnant = u['pregnant']
        expected_date = u['expected_date']
        previous_live_births = u["previous_live_births"]
        date_of_delivery = u['date_of_delivery']
        type_of_delivery = u['type_of_delivery']
        lactation_status = u['lactation_status']
        feeding = u['breast_feeding_status']
        COMPLICATION_STATUS = u['COMPLICATION_STATUS']
        complication_name = u['complication_name']
        vaccination_name = u['vaccination_name']
        try:
            cur = mysql.connection.cursor()
            cur.execute("select PREVIOUS_PREGNANCY_COMPLICATION_ID from PREVIOUS_PREGNANCY_COMPLICATIONS where "
                        "COMPLICATION_STATUS = %s",
                        (COMPLICATION_STATUS,))
            data = cur.fetchone()

            if data is None:
                return "No Details"
            cur.execute("select COMPLICATION_ID from PREGNANCY_COMPLICATIONS where COMPLICATION_NAME =%s",
                        (complication_name,))
            data1 = cur.fetchone()

            cur.execute("select VACCINATION_ID from PREGNANCY_VACCINATIONS where VACCINATION_NAME= %s",
                        (vaccination_name,))
            data2 = cur.fetchone()
            cur.execute("select PATIENT_LACTATING_ID from PREGNANCY_PATIENT_LACTATING_WOMEN "
                        "where LACTATING_STATUS=%s",
                        (lactation_status,))
            data3 = cur.fetchone()
            cur.execute("select PATIENT_BREAST_FEEDING_ID from PREGNANCY_BREAST_FEEDING "
                        "where BREAST_FEEDING_STATUS=%s",
                        (feeding,))
            data4 = cur.fetchone()

            if "PPC001" in data:
                cur = mysql.connection.cursor()
                cur.execute("insert into REG_PREGNANCY_DETAILS "
                            "(PREGNANT,EXPECTED_DELIVERY_DATE,PREVIOUS_LIVE_BIRTHS,"
                            "PREVIOUS_PREGNANCY_COMPLICATION_ID,VACCINATION_ID,COMPLICATION_ID,"
                            "PATIENT_LACTATING_ID,DATE_OF_DELIVERY,TYPE_OF_DELIVERY,PATIENT_BREAST_FEEDING_ID)"
                            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (pregnant, expected_date, previous_live_births, data,
                             data2, data1, data3, date_of_delivery, type_of_delivery,
                             data4))
                mysql.connection.commit()
                return "Successful"
            else:
                cur = mysql.connection.cursor()
                cur.execute("insert into REG_PREGNANCY_DETAILS "
                            "(PREGNANT,EXPECTED_DELIVERY_DATE,PREVIOUS_LIVE_BIRTHS,"
                            "PREVIOUS_PREGNANCY_COMPLICATION_ID,VACCINATION_ID,"
                            "PATIENT_LACTATING_ID,DATE_OF_DELIVERY,TYPE_OF_DELIVERY,PATIENT_BREAST_FEEDING_ID)"
                            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (pregnant, expected_date, previous_live_births, data,
                             data2, data3, date_of_delivery, type_of_delivery,
                             data4))
                mysql.connection.commit()
                return "Without Complication ID success"
        except ValidationError as e:
            print(e)
    return "invalid method"

    ##################################### VACCINATION ##########################################


@app.route('/VAC_Reg', methods=['POST'])
def VAC_Reg():
    if request.method == 'POST':
        YEARS = request.json['YEARS']
        VACCINE_NAME = request.json['VAC_NAME']
        try:
            cur = mysql.connection.cursor()
            cur.execute("select YEARS from VACCINATIONS where YEARS=%s", (YEARS,))
            data = cur.fetchone()

            cur.execute("select VACCINE_ID from VACCINATIONS  WHERE (YEARS=%s AND "
                        "VACCINE_NAME=%s)", (YEARS, VACCINE_NAME))
            data1 = cur.fetchone()

            Vaccinated = request.json['Vaccinated']
            cur.execute("select ID from COVID_VACCINE  WHERE (Vaccinated=%s)", (Vaccinated,))
            data2 = cur.fetchone()

            if "VC001" in data2:
                Dose = request.json['Dose']
                covid_vaccine_name = request.json['covid_vaccine_name']
                cur.execute("select ID from covid19_dose  WHERE (Dose=%s)", (Dose,))
                data3 = cur.fetchone()

                other_vaccine_name = request.json['other_vaccine_name']
                cur.execute("insert into REG_VAC_BOOKING"
                            "(ID,YEARS,VAC_NAME,VACCINATED,COVID_VAC_NAME,DOSE,OTHER_VAC_NAME)"
                            "values(null,%s,%s,%s,%s,%s,%s)",
                            (data, data1, data2, covid_vaccine_name, data3, other_vaccine_name))
                mysql.connection.commit()
            else:
                cur.execute("insert into REG_VAC_BOOKING(ID,YEARS,VAC_NAME,VACCINATED)"
                            "values(null,%s,%s,%s)", (data, data1, data2))
                mysql.connection.commit()
                return "Success"
        except ValidationError as e:
            print(e)
            return 'Successfully inserted Records'
    return 'invalid Parameters'

    ################################### Previous_health_issues ########################


@app.route("/HEALTH_ISSUES", methods=["POST"])
def health_issues():
    issue_name = request.json["issue_name"]
    TREATMENT_TAKEN_AT = request.json["TREATMENT_TAKEN_AT"]
    SURGERIES = request.json['SURGERIES']
    COMPLICATIONS_DURING_TREATMENT = request.json['COMPLICATIONS_DURING_TREATMENT']
    MEDICATIONS = request.json['MEDICATIONS']
    LIST_ANY_ALLERGIES_TO_MEDICATIONS = request.json['LIST_ANY_ALLERGIES_TO_MEDICATIONS']

    try:
        cur = mysql.connection.cursor()
        HIS_NAME = request.json['HIS_NAME']
        cur.execute("select HIS_ID from HEALTH_ISSUE  WHERE (HIS_NAME=%s)", (HIS_NAME,))
        HIS_ID = cur.fetchone()
        if "HIS001" in HIS_ID:
            Yes = HIS_ID
            cur.execute("select ISSUE_ID from HEALTH_ISSUES where (ISSUE_NAME = %s)",
                        (issue_name,))
            IssueName = cur.fetchone()
            if IssueName is None:
                return "No details in account"
            # Txn Table
            cur = mysql.connection.cursor()
            cur.execute(
                "insert into PREVIOUS_HEALTH_ISSUES( ISSUE_ID, TREATMENT_TAKEN_AT, SURGERIES, "
                "COMPLICATIONS_DURING_TREATMENT, MEDICATIONS, LIST_ANY_ALLERGIESTO_MEDICATIONS, "
                "HEALTH_ISSUE) values(%s, %s, %s, %s, %s, %s, %s)",
                (IssueName, TREATMENT_TAKEN_AT, SURGERIES, COMPLICATIONS_DURING_TREATMENT,
                 MEDICATIONS, LIST_ANY_ALLERGIES_TO_MEDICATIONS, Yes))
            mysql.connection.commit()
            return "Successfully Inserted with All Values", 200
        else:
            NO = 'HIS002'
            cur.execute(
                "insert into PREVIOUS_HEALTH_ISSUES( HEALTH_ISSUE) values(%s)",
                (NO))
            mysql.connection.commit()
            return "successfully inserted with no condition"
    except ValidationError as e:
        print(e)
        return jsonify(e.messages)


####################################### brain_disease########################################

@app.route('/REG_brain', methods=['POST'])
def REG_brain():
    BD_NAME = request.json['BD_NAME']
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("select BD_ID from BRAIN_DISEASES where BD_NAME=%s", (BD_NAME,))
    d = cur.fetchone()
    ac1 = d['BD_ID']
    cur.execute("select BD_ID from BRAIN_DISEASES where BD_NAME like 'YES'")
    dt = cur.fetchone()
    data = dt['BD_ID']
    if data in ac1:
        BRAIN_DISEASE_NAME = request.json['BRAIN_DISEASE_NAME']
        cur.execute("select BRAIN_DISEASES_ID from BRAIN_DISEASES_TYPES where BRAIN_DISEASE_NAME=%s",
                    (BRAIN_DISEASE_NAME,))
        d1 = cur.fetchone()
        ac2 = d1['BRAIN_DISEASES_ID']
        DISEASE_SYMPTOM_NAME = request.json['DISEASE_SYMPTOM_NAME']
        cur.execute("select DISEASE_SYMPTOM_ID from BRAIN_DISEASE_SYMPTOMS where BRAIN_DISEASE_ID=%s and "
                    "DISEASE_SYMPTOM_NAME=%s", (ac2, DISEASE_SYMPTOM_NAME,))
        d2 = cur.fetchone()
        ac3 = d2['DISEASE_SYMPTOM_ID']
        HAVE_DISEASE = request.json['HAVE_DISEASE']
        cur.execute("select FMD_ID from BRAIN_FAMILY_MEMBER where HAVE_DISEASE=%s", (HAVE_DISEASE,))
        d3 = cur.fetchone()
        ac4 = d3['FMD_ID']
        cur.execute("select FMD_ID from BRAIN_FAMILY_MEMBER where HAVE_DISEASE like 'YES'")
        d4 = cur.fetchone()
        data3 = d4['FMD_ID']
        if data3 in ac4:
            MEDICATIONS = request.json['MEDICATIONS']
            cur.execute("insert into REG_BRAIN_DETAILS(ID,BD_ID,BRAIN_DISEASES_ID,DISEASE_SYMPTOM_ID,FMD_ID,"
                        "MEDICATIONS) values(null,%s,%s,%s,%s,%s)", (ac1, ac2, ac3, ac4, MEDICATIONS,))
            mysql.connection.commit()
            return "user and family members have Brain disease"
        else:
            cur.execute(
                "insert into REG_BRAIN_DETAILS(ID,BD_ID,BRAIN_DISEASES_ID,DISEASE_SYMPTOM_ID,FMD_ID)"
                " values(null,%s,%s,%s,%s)", (ac1, ac2, ac3, ac4,))
            mysql.connection.commit()
            return "user have Brain disease but family members do not have Brain disease "
    else:
        HAVE_DISEASE1 = request.json['HAVE_DISEASE']
        cur.execute("select FMD_ID from BRAIN_FAMILY_MEMBER where HAVE_DISEASE=%s", (HAVE_DISEASE1,))
        d5 = cur.fetchone()
        ac5 = d5['FMD_ID']
        cur.execute("select FMD_ID from BRAIN_FAMILY_MEMBER where HAVE_DISEASE like 'YES'")
        d6 = cur.fetchone()
        data4 = d6['FMD_ID']
        if data4 in ac5:
            MEDICATIONS1 = request.json['MEDICATIONS']
            cur.execute(
                "insert into REG_BRAIN_DETAILS(ID,BD_ID, FMD_ID,MEDICATIONS)"
                " values(null,%s,%s,%s)", (ac1, ac5, MEDICATIONS1,))
            mysql.connection.commit()
            return "No Brain disease to user but family members have Brain disease "
        else:
            cur.execute(
                "insert into REG_BRAIN_DETAILS(ID,BD_ID, FMD_ID) values(null,%s,%s)", (ac1, ac5,))
            mysql.connection.commit()
            return " No Brain disease to user and family members"


##################################### KIDNEY DISEASE ######################################
@app.route('/Reg_kidney_disease', methods=["POST"])
def ptkd():
    patient_KD_status = request.json["patient_KD_status"]

    cur = mysql.connection.cursor()
    cur.execute("select KD_PATIENT_STATUS_ID from KIDNEY_DISEASE_PATIENT_STATUS where (KD_PATIENT_STATUS = %s)",
                (patient_KD_status,))
    data1 = cur.fetchone()

    #

    if "KDPSID001" in data1:
        symptoms = request.json["symptoms"]
        cur = mysql.connection.cursor()
        cur.execute("select KD_SYMPTOM_ID from KIDNEY_DISEASE_SYMPTOMS where ( KD_SYMPTOM_NAME= %s)", (symptoms,))
        data2 = cur.fetchone()

        patient_family_KD_status = request.json["patient_family_KD_status"]
        cur = mysql.connection.cursor()
        cur.execute("select KD_FAMILY_STATUS_ID from KIDNEY_DISEASE_FAMILY_STATUS where (KD_FAMILY_STATUS = %s)",
                    (patient_family_KD_status,))
        data3 = cur.fetchone()

        if "KD001" in data3:
            medications = request.json["medications"]
            cur = mysql.connection.cursor()

            cur.execute("insert into KIDNEY_DISEASE_BOOKING(KD_PATIENT_STATUS_ID,KD_SYMPTOM_ID,"
                        "KD_FAMILY_STATUS_ID,MEDICATIONS)" "values (%s,%s,%s,%s)",
                        (data1, data2, data3, medications))
            mysql.connection.commit()
            return "success"
        else:
            cur.execute(
                "insert into KIDNEY_DISEASE_BOOKING(KD_PATIENT_STATUS_ID,KD_SYMPTOM_ID,KD_FAMILY_STATUS_ID)" "values (%s,%s,%s)",
                (data1, data2, data3))
            mysql.connection.commit()
            return "values inserted successfully"

    else:
        patient_family_KD_status = request.json["patient_family_KD_status"]
        cur = mysql.connection.cursor()
        cur.execute("select KD_FAMILY_STATUS_ID from KIDNEY_DISEASE_FAMILY_STATUS where (KD_FAMILY_STATUS = "
                    "%s)",
                    (patient_family_KD_status,))
        data4 = cur.fetchone()
        if "KD001" in data4:
            medications1 = request.json["medications"]
            cur = mysql.connection.cursor()
            cur.execute("insert into KIDNEY_DISEASE_BOOKING(KD_PATIENT_STATUS_ID,KD_FAMILY_STATUS_ID,MEDICATIONS)"
                        "values (%s,%s,%s)", (data1, data4, medications1))
            mysql.connection.commit()
            return "success"
        else:
            cur.execute("insert into KIDNEY_DISEASE_BOOKING(KD_PATIENT_STATUS_ID,KD_FAMILY_STATUS_ID)"
                        "values(%s,%s)", (data1, data4))
            mysql.connection.commit()
            return "success"


##################################### EYE ######################################


@app.route('/REG_EYE', methods=['POST'])
def EYE_DISEASE():
    if request.method == 'POST':
        Disease = request.json['ED_TYPE_NAME']
        Symptom = request.json['SYMPTOM_NAME']
        cursor = mysql.connection.cursor()
        cursor.execute("select ED_TYPE_ID from PAT_HAS_EYE_DISEASE where ED_TYPE_NAME=%s", (Disease,))
        account = cursor.fetchone()
        h = "ED001"
        if h in account:
            cursor = mysql.connection.cursor()
            cursor.execute("select SYMPTOM_ID from EYE_DISEASE_SYMPTOMS where SYMPTOM_NAME=%s", (Symptom,))
            account1 = cursor.fetchone()

            Patient_Family = request.json['PFED_TYPE_NAME']
            cursor.execute("select PFED_TYPE_ID from PAT_FAMILY_HAS_EYE_DISEASE where PFED_TYPE_NAME=%s",
                           (Patient_Family,))
            account2 = cursor.fetchone()
            if "PFED001" in account2:
                medication = request.json['MEDICATIONS']
                medication1 = request.json['MEDICATIONS1']
                cursor.execute(
                    "insert into REG_EYE_DISEASE (PAT_HAS_ED,SYMPTOMS,PFM_HAS_ED,MEDICATIONS,MEDICATIONS1) "
                    "VALUES(%s,%s,%s,%s,%s)",
                    (account, account1, account2, medication, medication1))
                mysql.connection.commit()
                return "SUCCESS WITH YES CONDITIONS"
            else:
                medication2 = request.json['MEDICATIONS']
                cursor.execute(
                    "insert into REG_EYE_DISEASE (PAT_HAS_ED,SYMPTOMS,PFM_HAS_ED,MEDICATIONS) VALUES(%s,%s,%s,%s)",
                    (account, account1, account2, medication2))
                mysql.connection.commit()
                return "success with family no condition"

        else:
            Patient_Family = request.json['PFED_TYPE_NAME']
            cursor.execute("select PFED_TYPE_ID from PAT_FAMILY_HAS_EYE_DISEASE where PFED_TYPE_NAME=%s",
                           (Patient_Family,))
            account3 = cursor.fetchone()
            if 'PFED001' in account3:
                medication3 = request.json['MEDICATIONS1']
                cursor.execute("insert into REG_EYE_DISEASE (PAT_HAS_ED,PFM_HAS_ED,MEDICATIONS1) VALUES(%s,%s,%s)",
                               (account, account3, medication3))
                mysql.connection.commit()
                return "no and yes condition"
            else:
                cursor.execute("insert into REG_EYE_DISEASE (PAT_HAS_ED,PFM_HAS_ED) VALUES(%s,%s)",
                               (account, account3))
                mysql.connection.commit()
                return 'no and no condition'

    return 'invalid Parameters'

    ######################### ORTHO #########################


@app.route('/REG_ORTHO', methods=["POST", "GET"])
def Ortho_Disease():
    if request.method == 'POST':
        Disease = request.json['OD_TYPE_NAME']
        Symptom = request.json['SYMPTOM_NAME']
        Med = request.json['MEDICATIONS']
        cur = mysql.connection.cursor()
        cur.execute("select SYMPTOM_ID from ORTHO_DISEASE_SYMPTOMS where SYMPTOM_NAME=%s", (Symptom,))
        pqr = cur.fetchone()
        if pqr is None:
            return "please enter correct speciality"
        cur.execute("select OD_TYPE_ID from PAT_HAS_ORTHO_DISEASE where OD_TYPE_NAME=%s", (Disease,))
        abc = cur.fetchone()
        x = 'OD001'
        y = 'OD002'
        if x in abc:
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("insert into REG_ORTHO_DISEASE (PAT_HAS_OD,SYMPTOMS,MEDICATIONS) VALUES(%s,%s,%s)",
                        (abc, pqr, Med))
        if y in abc:
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("insert into REG_ORTHO_DISEASE (PAT_HAS_OD) VALUES(%s)", (abc,))
        mysql.connection.commit()
        cur.close()
        return 'successfully inserted'

        ################################### CANCER #####################################


@app.route('/REG_Cancer', methods=["POST"])
def Cancer():
    if 'patient_has_cancer' in request.json \
            and 'major_types' in request.json \
            and 'patient_family_cancer_status' in request.json \
            and 'medications' in request.json:
        patient_has_cancer = request.json["patient_has_cancer"]
        major_types = request.json["major_types"]
        patient_family_cancer_status = request.json["patient_family_cancer_status"]
        medications = request.json["medications"]

        cur = mysql.connection.cursor()
        cur.execute("select CANCER_STATUS_ID from CANCER_STATUS where (CANCER_STATUS = %s)", (patient_has_cancer,))
        data1 = cur.fetchone()
        if data1 is None:
            return "PLEASE ENTER THE CORRECT DETAILS"
        cur = mysql.connection.cursor()
        cur.execute("select CANCER_TYPE_ID from CANCER_MAJOR_TYPES where (CANCER_TYPES = %s)", (major_types,))
        data2 = cur.fetchone()
        if data2 is None:
            return "PLEASE SELECT THE CORRECT CANCER TYPE"
        cur = mysql.connection.cursor()
        cur.execute("select FAMILY_CANCER_STATUS_ID from CANCER_FAMILY_STATUS where (CANCER_STATUS = %s)",
                    (patient_family_cancer_status,))
        data3 = cur.fetchone()
        if data3 is None:
            return "PLEASE ENTER THE CORRECT DETAILS"
        if 'STID001' in data1:
            cur = mysql.connection.cursor()
            cur.execute(
                "insert into REG_CANCER_DETAILS(CANCER_STATUS_ID,CANCER_TYPE_ID,FAMILY_CANCER_STATUS_ID,"
                "CANCER_MEDICATIONS)"
                "values(%s,%s,%s,%s)", (data1, data2, data3, medications))
            mysql.connection.commit()
            return "successfully inserted", 200

        else:
            cur = mysql.connection.cursor()
            cur.execute(
                "insert into REG_CANCER_DETAILS(CANCER_STATUS_ID,FAMILY_CANCER_STATUS_ID,CANCER_MEDICATIONS)"
                "values(%s,%s,%s)", (data1, data3, medications))
            mysql.connection.commit()
        return "successfully inserted record", 200
    return 'Invalid parameter'

    ###################### THYROID ########################


@app.route('/REG_THYROID', methods=['POST'])
def thyroid_reg():
    if request.method == 'POST':
        user = request.json
        status = user['STATUS']
        try:
            cur = mysql.connection.cursor()
            cur.execute('select STATUS_ID from THYROID_STATUS where STATUS=%s', (status,))
            data = cur.fetchone()

            if data is None:
                return 'no data'

            if 'TSTID001' in data:
                sym_name = user['SYMPTOM_NAME']
                cur.execute('select SYMPTOM_ID from THYROID_SYMPTOMS where SYMPTOM_NAME=%s', (sym_name,))
                data1 = cur.fetchone()

                fam_status_name = user['THYROID_STATUS']
                cur.execute('select FAMILY_THYROID_STATUS_ID from THYROID_FAMILY_STATUS where THYROID_STATUS=%s',
                            (fam_status_name,))
                data2 = cur.fetchone()

                thyroidism = user['HYPO_THYROIDISM_OR_HYPER_THYROIDISM']
                medications = user['THYROID_MEDICATIONS']

                cur = mysql.connection.cursor()
                cur.execute(
                    'insert into REG_THYROID_DETAILS(STATUS_ID,SYMPTOM_ID,HYPO_THYROIDISM_OR_HYPER_THYROIDISM,'
                    'THYROID_FAMILY_STATUS_ID,THYROID_MEDICATIONS)VALUES(%s,%s,%s,%s,%s)',
                    (data, data1, thyroidism, data2, medications))
                mysql.connection.commit()
                return 'success'
            else:

                cur.execute('select STATUS_ID from THYROID_STATUS where STATUS=%s', (status,))
                data3 = cur.fetchone()
                fam_status_name = user['THYROID_STATUS']
                cur.execute('select FAMILY_THYROID_STATUS_ID from THYROID_FAMILY_STATUS where THYROID_STATUS=%s',
                            (fam_status_name,))
                data4 = cur.fetchone()
                # thyroidism = user['HYPO_THYROIDISM_OR_HYPER_THYROIDISM']
                cur.execute(
                    'insert into REG_THYROID_DETAILS(STATUS_ID,SYMPTOM_ID,HYPO_THYROIDISM_OR_HYPER_THYROIDISM,'
                    'THYROID_FAMILY_STATUS_ID,THYROID_MEDICATIONS)VALUES(%s,null,null,%s,null)',
                    (data, data4))
                mysql.connection.commit()

                if data3 is None:
                    return 'no data'
                if data3:
                    return 'no disease found'
        except ValidationError as e:
            return e.messages
    return 'invalid details'


############################ DIABETES ##############################


@app.route('/diabetes_reg', methods=['POST'])
def diabetes_reg():
    if request.method == 'POST':
        user = request.json
        status = user['DIABETIC_STATUS']
        try:
            cur = mysql.connection.cursor()
            cur.execute('select DIABETIC_STATUS_ID from DIABETIC_STATUS where DIABETIC_STATUS=%s', (status,))
            data = cur.fetchone()

            if data is None:
                return 'no data'

            if 'DSTID001' in data:
                sym_name = user['SYMPTOM_NAME']
                cur.execute('select SYMPTOM_ID from DIABETIC_SYMPTOMS where SYMPTOM_NAME=%s', (sym_name,))
                data1 = cur.fetchone()

                fam_status_name = user['DIABETIC_STATUS']
                cur.execute('select DIABETIC_FAMILY_STATUS_ID from DIABETIC_FAMILY_STATUS where DIABETES_F_STATUS=%s',
                            (fam_status_name,))
                data2 = cur.fetchone()

                diabete_type = user['DIABETES_TYPE1_OR_TYPE2']
                medications = user['DIABETES_MEDICATIONS']

                cur = mysql.connection.cursor()
                cur.execute('insert into REG_DIABETIC_DETAILS(DIABETES_STATUS_ID,SYMPTOM_ID,DIABETES_TYPE1_OR_TYPE2,'
                            'DIABETES_FAMILY_STATUS_ID,DIABETES_MEDICATIONS)VALUES(%s,%s,%s,%s,%s)',
                            (data, data1, diabete_type, data2, medications))
                mysql.connection.commit()
                return 'success'
            else:

                cur.execute('select DIABETIC_STATUS_ID from DIABETIC_STATUS where DIABETIC_STATUS=%s', (status,))
                data3 = cur.fetchone()
                fam_status_name = user['DIABETES_F_STATUS']
                cur.execute('select DIABETIC_FAMILY_STATUS_ID from DIABETIC_FAMILY_STATUS where DIABETES_F_STATUS=%s',
                            (fam_status_name,))
                data4 = cur.fetchone()
                cur.execute('insert into REG_DIABETIC_DETAILS(DIABETES_STATUS_ID,SYMPTOM_ID,DIABETES_TYPE1_OR_TYPE2,'
                            'DIABETES_FAMILY_STATUS_ID,DIABETES_MEDICATIONS)VALUES(%s,null,null,%s,null)',
                            (data, data4))
                mysql.connection.commit()

                if data3 is None:
                    return 'no data'
                if data3:
                    return 'no disease found'
        except ValidationError as e:
            return e.messages
    return 'invalid details'


########################### SKIN ###########################


@app.route('/REG_SKIN', methods=['POST'])
def Skin_reg():
    if request.method == 'POST':
        u = request.json
        disease_name = u['DISEASE_NAME']
        try:
            DISEASE_STATUS = u['DISEASE_STATUS']
            cur = mysql.connection.cursor()
            cur.execute('select DISEASE_ID from SKIN_DISEASE_DETAILS WHERE (DISEASE_STATUS=%s)',
                        (DISEASE_STATUS,))
            data = cur.fetchone()
            if "SKD01" in data:
                cur.execute("select * from SKIN_DISEASES where DISEASE_NAME = %s", (disease_name,))
                data1 = cur.fetchone()
                if data1 is None:
                    return "No Data"
                sym_name = data1[1]
                disease_name = data1[2]
                medication = u["medication"]
                cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cur.execute("insert into REG_SKIN_DETAILS (ID,SYMPTOM_NAME,DISEASE_NAME,SKIN_DISEASE_MEDICATIONS)"
                            "VALUES(%s,%s,%s,%s)", (data, sym_name, disease_name, medication))
                mysql.connection.commit()
                return "success"
            else:
                cur.execute('select DISEASE_ID from SKIN_DISEASE_DETAILS WHERE (DISEASE_STATUS=%s)',
                            (DISEASE_STATUS,))
                data3 = cur.fetchone()
                if data3 is None:
                    return "no data"
                if data3:
                    return "no symptoms and diseases"
        except ValidationError as e:
            print(e)
    return "invalid details"

    #################################### HAIR ##################################


@app.route('/REG_HAIR', methods=['POST'])
def REG_HAIR():
    if request.method == 'POST':
        u = request.json
        disease_name = u['DISEASE_NAME']

        try:
            DISEASE_STATUS = u['DISEASE_STATUS']
            cur = mysql.connection.cursor()
            cur.execute('select DISEASE_ID from HAIR_DISEASE_DETAILS WHERE (DISEASE_STATUS=%s)',
                        (DISEASE_STATUS,))
            data = cur.fetchone()
            if "HD001" in data:
                cur.execute("select * from HAIR_DISEASES where DISEASE_NAME = %s", (disease_name,))
                data1 = cur.fetchone()
                if data1 is None:
                    return "no data"
                sym_name = data1[1],
                disease_name = data1[2]
                medication = u["medication"]
                cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cur.execute(
                    "insert into REG_HAIR_DETAILS (ID,SYMPTOM_NAME,DISEASE_NAME,HAIR_DISEASE_MEDICATIONS)"
                    "VALUES(%s,%s,%s,%s)", (data, sym_name, disease_name, medication))
                mysql.connection.commit()
                return "success"
            else:
                cur.execute('select DISEASE_ID from HAIR_DISEASE_DETAILS WHERE (DISEASE_STATUS=%s)',
                            (DISEASE_STATUS,))
                data3 = cur.fetchone()

                if data3 is None:
                    return "no data"
                if data3:
                    return "no symptoms and diseases"
        except ValidationError as e:
            print(e)
        return "invalid details"


@app.route('/dental', methods=['POST'])
def dental():
    if request.method == 'POST':
        DD_NAME = request.json['DD_NAME']
        DDS_DISEASE = request.json['DDS_DISEASE']
        cur = mysql.connection.cursor()
        cur.execute("select DD_ID from DENTAL_DISEASES  WHERE (DD_NAME=%s)", (DD_NAME,))
        account = cur.fetchone()
        d = "DD001"
        if d in account:
            cur.execute("select DDS_ID from DENTAL_DISEASES_SYMPTOMS  WHERE (DDS_DISEASE=%s)", (DDS_DISEASE,))
            account1 = cur.fetchone()

            dd_medication = request.json['MEDICATIONS']
            cur.execute("insert into REG_DENTAL_BOOKING (DD_ID,DDS_ID,MEDICATIONS) values(%s,%s,%s)",
                        (account, account1, dd_medication))
            mysql.connection.commit()
        else:
            cur.execute("insert into REG_DENTAL_BOOKING (DD_ID) values(%s)", (account))
            mysql.connection.commit()

        return 'Successfully inserted'
    return 'invalid Parameters'

    ############################### HIV ######################


@app.route('/REG_HIV', methods=['POST'])
def HIV():
    if request.method == 'POST':
        PATIENT_HIV = request.json['PATIENT_HIV']
        HIV_SYMPTOM_NAME = request.json['HIV_SYMPTOM_NAME']
        cursor = mysql.connection.cursor()
        cursor.execute("select PHIV_ID from PATIENT_HIV  WHERE (PHIV_NAME=%s)", (PATIENT_HIV,))
        account = cursor.fetchone()
        h = "PH001"
        if h in account:

            cursor = mysql.connection.cursor()
            cursor.execute("select HIVS_ID from HIV_SYMPTOMS  WHERE (HIV_SYMPTOM_NAME=%s)", (HIV_SYMPTOM_NAME,))
            account1 = cursor.fetchone()

            FAMILY_HIV = request.json['FAMILY_HIV']
            cursor.execute("select FHIV_ID from FAMILY_HIV  WHERE (FHIV_NAME=%s)", (FAMILY_HIV,))
            account2 = cursor.fetchone()

            if account2 == "FH001":
                # medication = request.json['MEDICATIONS']
                medication = request.json['MEDICATIONS']
                cursor.execute("insert into REG_HIV_BOOKING(PHIV_ID,HIVS_ID,FHIV_ID,MEDICATIONS)"
                               "values(%s,%s,%s,%s)", (account, account1, account2, medication))
                mysql.connection.commit()
            else:
                medication1 = request.json['MEDICATIONS']
                cursor.execute("insert into REG_HIV_BOOKING(PHIV_ID,HIVS_ID,FHIV_ID,MEDICATIONS)"
                               "values(%s,%s,%s,%s)", (account, account1, account2, medication1))
                mysql.connection.commit()
        else:
            FAMILY_HIV1 = request.json['FAMILY_HIV']
            cursor.execute("select FHIV_ID from FAMILY_HIV  WHERE (FHIV_NAME=%s)", (FAMILY_HIV1,))
            account3 = cursor.fetchone()
            if 'FH001' in account3:
                medication2 = request.json['MEDICATIONS']
                cursor.execute("insert into REG_HIV_BOOKING(PHIV_ID,FHIV_ID,MEDICATIONS)"
                               "values(%s,%s,%s)", (account, account3, medication2))
                mysql.connection.commit()
            else:
                cursor.execute("insert into REG_HIV_BOOKING(PHIV_ID,FHIV_ID)""values(%s,%s)", (account, account3))
                mysql.connection.commit()

        return 'Successfully inserted'
    return 'invalid Parameters'


##################################### HEART ######################################
@app.route('/heart', methods=['POST'])
def heart():
    if request.method == 'POST':
        HA_PATIENT_STATUS = request.json['HA_PATIENT_STATUS']
        HA_SYMPTOM = request.json['HA_SYMPTOM']
        cursor = mysql.connection.cursor()
        cursor.execute("select HA_PATIENT_STATUS_ID from HEART_ATTACK_PATIENT_STATUS  WHERE (HA_PATIENT_STATUS=%s)",
                       (HA_PATIENT_STATUS,))
        account = cursor.fetchone()
        ha = 'HATK001'
        if ha in account:
            cursor = mysql.connection.cursor()
            cursor.execute("select HA_SYMPTOM_ID from HEART_ATTACK_SYMPTOMS  WHERE (HA_SYMPTOM=%s)", (HA_SYMPTOM,))
            account1 = cursor.fetchone()
            HEART_ATTACK_FAMILY_STATUS = request.json['HEART_ATTACK_FAMILY_STATUS']
            cursor.execute("select HA_FAMILY_STATUS_ID from HEART_ATTACK_FAMILY_STATUS  WHERE (HA_FAMILY_STATUS=%s)",
                           (HEART_ATTACK_FAMILY_STATUS,))
            account2 = cursor.fetchone()

            if "HAFSID001" == account2:
                # medication = request.json['MEDICATIONS']
                medication = request.json['MEDICATIONS']
                cursor.execute("insert into HEART_ATTACK_DETAILS(HA_PATIENT_STATUS_ID,HA_FAMILY_STATUS_ID,MEDICATIONS)"
                               "values(%s,%s,%s,%s)", (account, account1, account2, medication))
                mysql.connection.commit()
                return 'success'
            else:
                medication1 = request.json['MEDICATIONS']
                cursor.execute(
                    "insert into HEART_ATTACK_DETAILS(HA_PATIENT_STATUS_ID,HA_SYMPTOM_ID,HA_FAMILY_STATUS_ID,MEDICATIONS)"
                    "values(%s,%s,%s,%s)", (account, account1, account2, medication1))
                mysql.connection.commit()
                return 'success'
        else:
            HEART_ATTACK_FAMILY_STATUS = request.json['HEART_ATTACK_FAMILY_STATUS']
            cursor.execute("select HA_FAMILY_STATUS_ID from HEART_ATTACK_FAMILY_STATUS  WHERE (HA_FAMILY_STATUS=%s)",
                           (HEART_ATTACK_FAMILY_STATUS,))
            account3 = cursor.fetchone()
            if 'HAFSID001' in account3:

                medication2 = request.json['MEDICATIONS']
                cursor.execute("insert into HEART_ATTACK_DETAILS(HA_PATIENT_STATUS_ID,HA_FAMILY_STATUS_ID,MEDICATIONS)"
                               "values(%s,%s,%s)", (account, account3, medication2))
                mysql.connection.commit()
                return 'success'

            else:
                cursor.execute("insert into HEART_ATTACK_DETAILS(HA_PATIENT_STATUS_ID,HA_FAMILY_STATUS_ID)"
                               "values(%s,%s)", (account, account3))
                mysql.connection.commit()
                return 'success'

    return 'invalid Parameters'


if __name == "__main__":
    app.run(debug=True)
