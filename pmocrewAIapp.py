import os
from crewai import Agent, Task, Crew, process

os.environ["OPENAI_API_KEY"] = ("")

# You can choose to use a local model through Ollama for example.
#
# from langchain.llms import Ollama
# ollama_llm = Ollama(model="openhermes")

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

from langchain.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

# Define your agents with roles and goals
researcher = Agent(
  role='Senior Project Manager',
  goal='Ensure efficient financial and operational control of the project to land three NASA and SpaceX astronauts on Mars in 2025',
  backstory="""With a robust background in project management within aerospace industries, 
  you have been at the forefront of pioneering projects. Your journey includes significant experience at NASA and SpaceX, 
  where you have been instrumental in advancing space exploration missions. Known for your exceptional ability to manage complex, high-stakes projects, 
  you have been entrusted with the historic Mars landing mission. Your expertise in Earned Value Management ensures projects stay on budget and on time, 
  while your proficiency in Agile methodologies fosters adaptability and innovation in project execution. This mission is not just a career highlight; 
  it's a pivotal moment in human space exploration, and your leadership is crucial to its success.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool]
  # You can pass an optional llm attribute specifying what mode you wanna use.
  # It can be a local model through Ollama / LM Studio or a remote
  # model like OpenAI, Mistral, Antrophic of others (https://python.langchain.com/docs/integrations/llms/)
  #
  # Examples:
  # llm=ollama_llm # was defined above in the file
  # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7)
)
writer = Agent(
  role='Project Controller',
  goal='Ensure efficient financial and operational control of the project to land three NASA and SpaceX astronauts on Mars in 2025',
  backstory="""As a Project Controller with extensive experience in the aerospace sector, 
  your journey has been marked by your ability to manage complex budgets and operations effectively. 
  With a background in overseeing large-scale projects at organizations like NASA and SpaceX, 
  you have developed a keen eye for detail and a deep understanding of the financial and operational intricacies of space missions. 
  Your role is critical in ensuring that the Mars mission remains within budget and operational constraints, 
  maintaining the balance between ambitious space exploration goals and practical resource management.""",
  verbose=True,
  allow_delegation=True,
  # (optional) llm=ollama_llm
)
# Create tasks for your agents
task1 = Task(
  description="""Develop a comprehensive project management plan for the Mars mission scheduled for 2025. The Contract Start Date is April 1, 2024. The total budget for this mission is set at $969 million. The project operates under a Cost Plus Fixed Fee Contract, which implies careful budget management and accurate reporting of expenses are crucial. With a team of 10 highly skilled professionals, you need to ensure that the project stays within budget while meeting all technical and safety standards. The plan should detail timelines, resource allocation (including personnel and equipment), technical requirements, collaboration strategies with NASA and SpaceX, risk management, and contingency plans. Your final deliverable MUST be a detailed project plan that outlines a clear roadmap for the successful and cost-effective completion of the mission, adhering to the specified budget and contract terms.""",
  agent=researcher
)

task2 = Task(
  description="""Conduct a comprehensive analysis of the budgetary and operational aspects of the Mars mission planned for 2025. Your comprehensive responsibilities include:
Budgetary and Operational Analysis: Conduct an in-depth analysis of the mission's financial and operational elements. Identify areas for financial efficiency and operational risks. Evaluate adherence to Earned Value Management (EVM) principles and the effectiveness of resource allocation, considering the specific budget and contract type.
Project Schedule Creation: Develop a detailed project schedule in a table format. This schedule should include the following columns:
-Task ID
-Work Breakdown Structure (WBS)
-Task Name
-Start Date
-Finish Date
-% Complete
-Predecessors
-Successors
-Total Slack
-Start Variance
-Finish Variance
The schedule should comprehensively cover all tasks and milestones, ensuring that every aspect of the project is accounted for. This schedule will be crucial in tracking progress, identifying potential delays, and managing dependencies between different tasks.
Compliance and Reporting: Ensure compliance with the Cost Plus Fixed Fee contract terms and prepare regular financial reports to stakeholders. The reports should include insights from your EVM analysis and updates on the project's financial health.You are responsible for overseeing the financial and operational integrity of the Mars mission scheduled for 2025, with a total budget of $969 million under a Cost Plus Fixed Fee Contract. Your task is to conduct an in-depth analysis of the mission's budgetary and operational components. This includes identifying areas where financial efficiency can be maximized and pinpointing potential operational risks. Assess how well the project adheres to Earned Value Management (EVM) principles to ensure cost and schedule performance are on track. Additionally, evaluate the effectiveness of resource allocation strategies, ensuring optimal utilization of the allocated budget and personnel resources. Your analysis should also cover compliance with the contractual terms of the Cost Plus Fixed Fee arrangement. The final deliverable MUST be a comprehensive analysis report that details the financial health of the project, evaluates risk management practices, and provides operational insights. This report will play a crucial role in guiding financial decisions and operational adjustments to enhance the likelihood of the mission's success.
Your task involves detailed planning and tracking of budgets, schedules, and resources for your control accounts. You are expected to implement Earned Value Management (EVM) principles to accurately monitor cost and schedule performance, identify variances, and predict future performance. 

    Key responsibilities include:
    - Establishing and maintaining control account plans, including budgets and schedules.
    - Coordinating with different teams to ensure alignment of technical and financial aspects.
    - Regularly reviewing and analyzing the performance of control accounts against planned values.
    - Identifying and managing risks associated with cost and schedule overruns.
    - Reporting control account status to higher management and making recommendations for corrective actions where necessary.
    
    Your final deliverable is a comprehensive control account report that includes performance analysis, risk assessment, and recommendations for maintaining the project within the stipulated budget and timeframes, while meeting all technical requirements.""",
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