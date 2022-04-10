import sqlalchemy
print(sqlalchemy.__version__)

from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("mysql+pymysql://root:password@localhost/library", echo=False, future=True)

with engine.connect() as conn:
    conn.execute(
        text("INSERT INTO staff(staff_id, employee_number, staff_name, phone, email, branch_id, job_role, salary, national_insurance) VALUES(:staff_id, :employee_number, :staff_name, :phone, :email, :branch_id, :job_role, :salary, :national_insurance)"),
       [{"staff_id": 1, "employee_number": 2, "staff_name": "Tim", "phone": 774859037, "email": "tim@sky.com", "branch_id": 1, "job_role": "cleaner", "salary": 2000, "national_insurance": "JZ756TH"}]
       {"staff_id": 2, "employee_number": 3, "staff_name": "Adila", "phone": 774859038, "email": "adila@sky.com","branch_id": 2, "job_role": "engineer", "salary": 1000, "national_insurance": "JZ75647"},
       {"staff_id": 3, "employee_number": 4, "staff_name": "Liam", "phone": 77485985, "email": "liam@sky.com", "branch_id": 3, "job_role": "engineer", "salary": 200, "national_insurance": "JZ7567"},
       {"staff_id": 4, "employee_number": 5, "staff_name": "Alex", "phone": 774859084, "email": "alex@sky.com", "branch_id": 4, "job_role": "engineer", "salary": 8900, "national_insurance": "JZ47647"},
        {"staff_id": 5, "employee_number": 6, "staff_name": "Liv", "phone": 77484538, "email": "liv@sky.com", "branch_id": 5, "job_role": "engineer", "salary": 4000, "national_insurance": "JZ74747"},
       {"staff_id": 6, "employee_number": 7, "staff_name": "Linda", "phone": 774892038, "email": "linda@sky.com", "branch_id": 6, "job_role": "engineer", "salary": 3000, "national_insurance": "JZ49647"},
        {"staff_id": 7, "employee_number": 8, "staff_name": "Hannah", "phone": 774855038, "email": "hannah@sky.com", "branch_id": 8, "job_role": "doctor", "salary": 4000, "national_insurance": "J585647"},
        {"staff_id": 8, "employee_number": 9, "staff_name": "Sara", "phone": 774859038, "email": "sara@sky.com", "branch_id": 9, "job_role": "engineer", "salary": 1000, "national_insurance": "JZ75647"},
        {"staff_id": 9, "employee_number": 10, "staff_name": "Adila", "phone": 774859038, "email": "adila@sky.com", "branch_id": 10, "job_role": "engineer", "salary": 1000, "national_insurance": "JZ75647"},
        {"staff_id": 10, "employee_number": 10, "staff_name": "Henry", "phone": 774885838, "email": "henry@sky.com","branch_id": 2, "job_role": "engineer", "salary": 1000, "national_insurance": "JZ75647"}]

       # text("INSERT INTO branch(branch_id, branch_number, branch_phone, branch_address, branch_annual_budget) VALUES(:branch_id, :branch_number, :branch_phone, :branch_address, :branch_annual_budget)"),
      #  [{"branch_id": 2, "branch_number": 1, "branch_phone":1245, "branch_address": "Leeds", "branch_annual_budget": 200},
      #   [{"branch_id": 3, "branch_number": 2, "branch_phone":1250, "branch_address": "London", "branch_annual_budget": 300},
      #   {"branch_id": 4, "branch_number": 3, "branch_phone":1251, "branch_address": "London", "branch_annual_budget": 400},
      #   {"branch_id": 5, "branch_number": 4, "branch_phone":1252, "branch_address": "Scotland", "branch_annual_budget": 500},
      #   {"branch_id": 6, "branch_number": 5, "branch_phone": 1253, "branch_address": "Scotland","branch_annual_budget": 600},
      #   {"branch_id": 7, "branch_number": 6, "branch_phone": 1254, "branch_address": "Wales", "branch_annual_budget": 700},
      #   {"branch_id": 8, "branch_number": 7, "branch_phone": 1255, "branch_address": "London", "branch_annual_budget": 300},
     #    {"branch_id": 9, "branch_number": 8, "branch_phone": 1256, "branch_address": "Sheffield", "branch_annual_budget": 800},
       #  {"branch_id": 10, "branch_number":9, "branch_phone": 1259, "branch_address": "London", "branch_annual_budget": 1000}]

        )
    conn.commit()

