import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from prettytable import PrettyTable
x = PrettyTable()

os.environ["OPENAI_API_KEY"] = ""
os.environ["SERPER_API_KEY"] = "" # serper.dev API key

# You can choose to use a local model through Ollama for example. See https://docs.crewai.com/how-to/LLM-Connections/ for more information.

# os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
# os.environ["OPENAI_MODEL_NAME"] ='openhermes'  # Adjust based on available model
# os.environ["OPENAI_API_KEY"] ='sk-111111111111111111111111111111111111111111111111'

search_tool = SerperDevTool()

# Define your agents with roles and goals
researcher = Agent(
  role='Senior Project Manager',
  goal='Ensure efficient cost, schedule, performance, risk, and execution of the project to land 3 NASA and 3 SpaceX astronauts on Mars in August 11, 2025',
  backstory="""You work at a leading tech think tank.
  Your expertise lies in leading special projects.
  You have a knack for dissecting complex earned value management metrics and presenting to stakeholders.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool]
  # You can pass an optional llm attribute specifying what mode you wanna use.
  # It can be a local model through Ollama / LM Studio or a remote
  # model like OpenAI, Mistral, Antrophic or others (https://docs.crewai.com/how-to/LLM-Connections/)
  #
  # import os
  # os.environ['OPENAI_MODEL_NAME'] = 'gpt-3.5-turbo'
  #
  # OR
  #
  # from langchain_openai import ChatOpenAI
  # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7)
)
writer = Agent(
  role='Senior Project Controller',
  goal='Develop a project schedule that includes a hybrid approach such as Agile and Earned Value Management',
  backstory="""You are a renowned Project Controller, known for your technical expertise in complex project schedules.
  You transform complex project schedule metrics in projects of all sizes.""",
  verbose=True,
  allow_delegation=True
)

# Create tasks for your agents
task1 = Task(
  description="""Develop an Integrated Project Management (IPM) Maturity and Environment Total 
  Risk Rating (METRR) using Earned Value Management which is an assessment mechanism developed as part of a
  Department of Energy-sponsored joint research study led by Arizona State University and representing more
  than fifteen government and industry organizations for a Project named "Project Adam". The Start of Project Adam
  is April 1, 2024 and the Launch Date is August 11, 2025.

  The tool assesses a spectrum of EVMS maturity and environment issues centered around the thirty-two EIA-748 EVMS Guidelines, while also referencing
  PMI's ANSI Standard for EVM (2019) and ISO 21508:2018 guidance. By using the IPM METRR (pronounced “IPM meter”)
  to assess both the maturity and environment of Project Adam's EVMS, project leaders and personnel
  can understand the efficacy of their EVMS to support integrated project management. It also helps identify opportunities for
  improvement. The ultimate goal of performing this assessment is to assure project adam participants
  are working with accurate, timely, and reliable information to manage their work, leading to successful
  project performance to landing 3 NASA and 3 SpaceX astronauts on Mars in August 11, 2025.

  It is very crucial to monitor the environment and climate on Mars, by doing so, this will the success and
  forecast any delays to the launch date. You MUST use this website called the Mars Weather Mission Webpage
  to gather weather and  climate data: https://mars.nasa.gov/msl/mission/weather/
  # categories = [
      {
          "Category": "Culture",
          "Description": "The culture category addresses those issues that impact the project culture. Culture is, by definition, the display of behaviors. Organizational culture is a system of common assumptions, values and beliefs (or the lack thereof) that governs how people behave in organizations. Organizational values and beliefs should align with the development and outcomes of a successful EVMS. The project culture can enable or hinder the effectiveness of the EVMS.",
          "Factors for Review": [
          "1a. The contractor organization is supportive and committed to EVMS implementation, including making the necessary investments for regular maintenance and self-governance.",
          "1b. The project culture fosters trust, honesty, transparency, communication, and shared values across functions.",
          "1c. The customer organization is supportive and committed to the implementation and use of EVMS.",
          "1d. Project leaders make timely and transparent decisions informed by the EVMS.",
          "1e. The project leadership effectively manages and controls change using EVMS, including corrective actions and continuous improvement.",
          "1f. Effective teamwork exists, and team members are working synergistically toward common project goals.",
          "1g. Alignment and cohesion exist among key team members who implement and execute EVMS, including common objectives and priorities."
          ]
      },
      {
          "Category": "People",
          "Description": "The people category addresses the individuals who represent the interests of their respective stakeholders (e.g., project business manager, project control analyst, project schedule analyst, acquisitions/subcontracts, control account manager, Integrated Project Team (IPT) or line/resource management) and are adept in the relevant subject matter, in order to contribute to the process that leads to favorable project control outcomes.",
          "Factors for Review": [
          "2a. The contractor team is experienced and qualified in implementing and executing the EVMS.",
          "2b. The customer team is experienced in understanding and using EVM results to inform decision-making.",
          "2c. Project leadership is defined, effective, and accountable.",
          "2d. Project stakeholder interests are appropriately represented in the implementation and execution of the EVMS.",
          "2e. Professional learning and education of key individuals responsible for EVMS implementation and execution, is appropriate to meet project requirements.",
          "2f. Team members responsible for the EVMS implementation and execution phases are co-located and/or accessible."
          ]
      },
      {
          "Category": "Practices",
          "Description": "The practices category addresses internal and external procedures and processes that can positively or negatively influence the outcome of a project or program. Internal business practices and methods are specific to a given organization, including internal standards, requirements and best practices. External business practices, regulations, requirements, procedures and methods are across organizational boundaries.",
          "Factors for Review": [
          "3a. The project promotes and follows standard practices to implement and execute an EVMS.",
          "3b. EVMS requirements definition is in place, and agreement exists among key stakeholders and customer.",
          "3c. Roles and responsibilities are defined, documented and well-understood for implementing and executing EVMS.",
          "3d. Communication is open and effective, including consistent terminology, metrics, and reports.",
          "3e. Effective oversight is in place and used, including internal and external surveillance and independent reviews.",
          "3f. Contractual terms and conditions that impact the effectiveness of EVMS are known and have been addressed.",
          "3g. Appropriate Subject Matter Expert (SME) input is adequate and timely.",
          "3h. Coordination exists between the key disciplines involved in implementing and executing the EVMS."
          ]
      },
      {
          "Category": "Resources",
          "Description": "The resources category addresses the availability of key tools, data, funding, time, personnel, and technology/software to support the EVMS sub-processes.",
          "Factors for Review": [
          "4a. Adequate technology/software and tools are integrated and used for the EVMS.",
          "4b. Sufficient funding is committed and available for implementing and executing the EVMS.",
          "4c. The team that implements and executes the EVMS for the project/program is adequate in size and composition.",
          "4d. Sufficient calendar time and work hours are committed and available for implementing and executing the EVMS.",
          "4e. Data are readily available to populate EVMS tools supporting analyses for decision-making.",
          "4f. The project utilizes an appropriate periodic cycle for executing the EVMS effectively and efficiently."
          ]
      }
  ]

  table = PrettyTable()
  table.field_names = ["Category", "Description", "Factors for Review"]

  for category in categories:
      table.add_row([category["Category"], category["Description"], (category["Factors for Review"])])

  print(table)

  MUST Debate and determine probability of success: Both the Senior Project Manager and the Project Controller must review all reports then will debate amongst each other to determine a final forecast of landing on Mars
  on the target date of August 11, 2025, along with a probability of success between 0 percent - 100 percent.""",
  expected_output="Full analysis Integrated Project Management (IPM) Maturity and Environment Total Risk Rating (METRR) Report",
  agent=researcher
)

task2 = Task(
  description="""Conduct a comprehensive cost and schedule health analysis to the project schedule of the cost, key milestones, and operational aspects of the 
  Mars mission planned for August 11, 2025. Your responsibilities include:
  # Cost Estimating: Conduct an in-depth cost esitmating analysis of the mission's cost, key milestones and operational elements. Identify areas for financial efficiency and operational risks.
    Evaluate adherence to Earned Value Management (EVM) principles and the effectiveness of resource allocation,considering the specific budget and contract type. The resources are working a 40 hour work week with weekends off.
    schedule variances and performance indicators. Develop recommendations for improvements based on findings.
    Communication Plan: Develop a communication plan to ensure all relevant stakeholders understand the project's status.

  # Schedule Management Plan: Develop a detailed Schedule Management Plan (SMP), which includes all key project activities, dependencies, resources required, duration estimates, and critical success factors.
    Monitor progress against the SMP and report any deviations or delays promptly. Ensure that all team members understand their roles and how they contribute to achieving the plan objectives
    Monitor progress against the SMP and report any deviations or delays promptly. Ensure that the team stays on track with the plan and identify potential causes of delay or cost overruns.

  # Project Schedule: Develop a Project Schedule that illustrates how tasks will be completed over time.
    x = PrettyTable()
    x.field_names = ["Task ID #", "WBS", "Task Name", "% Complete", "Start Date", "Finish Date", "Duration", "Actual Start Date", "Actual Finish Date", "Resource Assignment", "Predecessors", "Successors", "Total Slack"]
    x.add_row(["", 1295, 1158259, 600.5])
    x.add_row(["", 5905, 1857594, 1146.4])
    x.add_row(["", 112, 120900, 1714.7])
    x.add_row(["", 1357, 205556, 619.5])
    x.add_row(["", 2058, 4336374, 1214.8])
    x.add_row(["", 1566, 3806092, 646.9])
    x.add_row(["", 5386, 1554769, 869.4])

    print(table)

  # Final Assessment:
  senior_project_manager_assessment = "The Senior Project Manager assesses the probability of success for the Mars mission as "" and rates it as likely to ""."
  project_controllers_assessment = "The Project Controllers assess the probability of success for the Mars mission as "" and rates it as highly likely to ""."

  The Integrated Master Schedule should comprehensively cover all tasks and milestones, ensuring that every aspect of the project is accounted for.This Integrated Master Schedule will be crucial in tracking progress, performance, identifying potential delays, and 
  managing dependencies between different tasks.

  # Risk Management Plan: Develop a Quantitative Risk Management Plan (RMP) that identifies project risks, risk mitigation strategies, and responsible
  allocating sufficient resources to complete each task within its estimated timeframe. Utilize a Risk Assessment Form to record risks identified during risk assessments conducted by project stakeholders
  Assigning appropriate resources to each task.  Utilize a Risk Cube with Levels of Risks (1-Very Low, 2-Low, 3-Medium, 4-High, 5-Very High) approach to manage risks associated with each project task. The risk cube should include columns for Task,
  Assigning appropriate resources to each task.

  # Compliance and Reporting: Ensure compliance with the Cost Plus Fixed Fee contract terms and prepare regular financial reports to stakeholders. The reports should include insights from your EVM analysis and updates on the project's financial health.
  You are responsible for overseeing the financial and operational integrity of the Mars mission scheduled for August 11, 2025, with a total budget of $969 million under a Cost Plus Fixed Fee Contract. Your task is to conduct an in-depth analysis of the mission's 
  budgetary and operational components. This includes identifying areas where financial efficiency can be maximized and pinpointing potential operational risks. Assess how well the project adheres to Earned Value Management (EVM) principles to ensure cost and 
  schedule performance are on track. Additionally, evaluate the effectiveness of resource allocation strategies, ensuring optimal utilization of the allocated budget and personnel resources. Your analysis should also cover compliance with the contractual terms 
  of the Cost Plus Fixed Fee arrangement. The final deliverable MUST be a comprehensive analysis report that details the financial health of the project, evaluates risk management practices, and provides operational insights. This report will play a crucial role in guiding 
  financial decisions and operational adjustments to enhance the likelihood of the mission's success.
  Your task involves detailed planning and tracking of budgets, schedules, and resources for your control accounts. 
  You are expected to implement Earned Value Management (EVM) principles to accurately monitor cost and schedule performance, identify variances, and predict future performance. 
  Key responsibilities include:
    - Establishing and maintaining control account plans, including budgets and schedules.
    - Coordinating with different teams to ensure alignment of technical and financial aspects.
    - Regularly reviewing and analyzing the performance of control accounts against planned values.
    - Identifying and managing risks associated with cost and schedule overruns.
    - Reporting control account status to higher management and making recommendations for corrective actions where necessary.
  Your final deliverable is a detailed report of the current status of the project schedule, along with a cost analysis report.

  # Calculate PERT by using this PERT Formula: Pert Estimate = (Optimistic + (4 X Most Likely) + Pessimistic)/6.

  # MUST Debate and determine probability of success: Both the Senior Project Manager and the Project Controller must review all reports then will debate amongst each other to determine a final forecast of landing on Mars 
  on the target date of August 11, 2025, along with a probability of success between 0 percent - 100 percent.""",
  expected_output="Monte Carlo Analysis Report and Project Status Report",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)