from pydantic_ai import Agent, RunContext
from app2.advisor.models import Profile, ReportResult

fitness_agent = Agent(
    'gpt-4o',
    deps_type=Profile,
    result_type=ReportResult,
    result_retries=3,
    system_prompt="Create personalized ReportResult based on user's information provided "
                  "for motivational quotes call the get_motivation tool and pick the single best one from the list"
)

motivation_agent = Agent(
    'gpt-4o',
    result_type=list[str],
    system_prompt="Give motivational quotes based on the user's fitness goals and current status."
)

@fitness_agent.system_prompt
async def add_user_fitness_data(ctx: RunContext[Profile]) -> str:
    data = ctx.deps
    return f"User fitness profile and goals: {data!r}"

@fitness_agent.tool
async def get_motivation(ctx: RunContext) -> list[str]:
    return await motivation_agent.run(f"Please generate 5 motivational quotes about working out and eating healthy.")

async def analyze_profile(profile: Profile) -> ReportResult:
    result = await fitness_agent.run("Create a personalized fitness and nutrition plan.", deps=profile)
    return result.output