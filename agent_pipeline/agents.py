from crewai import Agent, LLM
from .tools import tool
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY=os.getenv("api-key-techsage")

# ✅ Explicit provider declaration for Gemini

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
)
# Researcher Agent
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of innovation, "
        "eager to explore and share knowledge that could change the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Writer Agent
news_writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
