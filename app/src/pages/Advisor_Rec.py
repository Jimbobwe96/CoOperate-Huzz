import requests
import streamlit as st

st.set_page_config(layout="wide")  # Makes the page wider

st.session_state['advisor_id'] = 1

col1, col2 = st.columns([9, 2])
with col2:
    if st.button("Back"):
        st.switch_page('pages/Advisor_Home.py')

try:
    advisor_id = st.session_state['advisor_id']
    response = requests.get(f'http://api:4000/s/students/advisor/{str(advisor_id)}')
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns a JSON list of reviews
    else:
        st.error(f"Error fetching data from API: {response.status_code}")
except Exception as e:
    st.write("**Important**: Could not connect to sample API, so using dummy data.")
    data = [
        {"Company": "Joe", "Role": "Joe", "Location": "MA", "Pay": 9999,
         "Required GPA": 3.0, "Culture": 3, "Satisfaction": 4,
         "Compensation": 2, "Learning": 2, "Work Life Balance": 1},
    ]
students = []
if data:
    for item in data:
        student_id = item.get('StudentID')
        full_name = item.get('FirstName') + " " + item.get('LastName')
        gpa = item.get('GPA')
        major = item.get('Major')
        cur_year = item.get('CurrentYear')

        students.append({
            "id": student_id,
            "full_name": full_name,
            "gpa": gpa,
            "major": major,
            "year": cur_year
        })

# --- Fetch Coop Roles ---
try:
    response_coop = requests.get('http://api:4000/cr/coop_role')
    if response_coop.status_code == 200:
        coop_data = response_coop.json()
    else:
        st.error(f"Error fetching coop roles: {response_coop.status_code}")
        coop_data = []
except Exception:
    st.write("**Important**: Could not connect to API for coop roles, using dummy data.")
    coop_data = [
        {"position_id": 101, "title": "Software Intern", "company": "ABC Corp", "description": "Coding tasks"},
        {"position_id": 102, "title": "Data Analyst Intern", "company": "XYZ Data", "description": "Analyze data"}
    ]

coop_roles = []
for role in coop_data:
    position_id = role.get('PositionID')
    company_id = role.get('CompanyID')
    title = role.get('Role', '')
    company = role.get('Company', '')
    location = role.get('Location', '')
    pay = role.get('Pay', '')
    req_gpa = role.get('Required GPA', '')

    coop_roles.append({
        "position_id": position_id,
        "company_id": company_id,
        "title": title,
        "company": company,
        "location": location,
        "pay": pay,
        "req_gpa": req_gpa
    })

# --- Sidebar: Student Selection ---
st.sidebar.title("Select a Student")
student_names = [s["full_name"] for s in students]

if not student_names:
    st.error(student_names)
    st.error("No students available for this advisor.")
    st.stop()

selected_student_name = st.sidebar.selectbox("Students:", student_names)
selected_student = next((s for s in students if s["full_name"] == selected_student_name), None)
selected_student_id = selected_student["id"] if selected_student else None

# --- Main Page Layout ---
st.markdown("<h1 style='white-space: nowrap;'>Student Details and Coop Roles</h1>", unsafe_allow_html=True)

# Top bar for filtering by company
companies = sorted(set(r["company"] for r in coop_roles))
company_list = ["All"] + companies
selected_company = st.selectbox("Filter by company:", company_list)

# Filter roles by selected company
if selected_company == "All":
    filtered_roles = coop_roles
else:
    filtered_roles = [r for r in coop_roles if r["company"] == selected_company]

# Create columns: left for student details, right for roles
col1, col2 = st.columns([2,3])

# --- Left Column: Student Details ---
with col1:
    if selected_student:
        st.subheader("Student Details")
        st.write(f"**Name:** {selected_student['full_name']}")
        st.write(f"**GPA:** {selected_student['gpa']}")
        st.write(f"**Major:** {selected_student['major']}")
        st.write(f"**Year:** {selected_student['year']}")

# --- Right Column: Filtered Coop Roles ---
with col2:
    st.subheader("Coop Roles")
    if filtered_roles:
        for role in filtered_roles:
            f_position_id = role["position_id"]
            f_company_id = role["company_id"]
            f_title = role["title"]
            f_company = role["company"]
            f_location = role["location"]
            f_pay = role["pay"]
            f_req_gpa = role["req_gpa"]

            colcr, colb = st.columns([3,1])
            with colcr:
                st.markdown(
                        f"""
                        <div style="
                            border: 1px solid #ccc;
                            border-radius: 8px;
                            padding: 15px;
                            margin: 10px auto; 
                            background-color: #f9f9f9;
                            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                        ">
                            <h4 style="margin: 0; font-size: 20px;">{f_company}</h4>
                            <p style="font-size: 16px; margin: 10px 0 0 0;">{f_title}</p>
                            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Location: </strong> {f_location}</p>
                            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Pay: </strong> {f_pay}</p>
                            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Required GPA: </strong> {f_req_gpa}</p>
                                                                                    
                        </div>
                        """,
                        unsafe_allow_html=True
                    ) 
                with colb:
                    # --- Recommend Button ---
                    if st.button(f"Recommend ID({f_position_id}) to Student"):
                        if not selected_student_id:
                            st.error("Please select a student")
                        else:
                            data = {
                                "student_id": selected_student_id,
                                "position_id": f_position_id,
                                "company_id": f_company_id
                            }
                            try:
                                response = requests.put("http://api:4000/s/recommend", json=data)
                                if response.status_code == 200:
                                    st.success("Recommendation successfully recorded!")
                                else:
                                    st.error(f"Failed to recommend. Server responded with status {response.status_code}.")
                            except Exception as e:
                                st.error(f"Error sending request: {e}")
    else:
        st.warning("No Coop Roles found for the selected company.")
        selected_position_id = None

st.write("---")

# --- Recommend Button ---
if st.button("Recommend to Student"):
    if not selected_student_id or not selected_position_id:
        st.error("Please select both a student and a CoopRole.")
    else:
        payload = {
            "student_id": selected_student_id,
            "position_id": selected_position_id
        }
        try:
            put_response = requests.put("http://api:4000/s/recommend", json=payload)
            if put_response.status_code == 200:
                st.success("Recommendation successfully recorded!")
            else:
                st.error(f"Failed to recommend. Server responded with status {put_response.status_code}.")
        except Exception as e:
            st.error(f"Error sending request: {e}")