import os
from dotenv import load_dotenv
from talkingheads import ChatGPTClient, MultiAgent

load_dotenv()

# base_browser
# chathead = ChatGPTClient(
#     headless=False,
#     incognito=False,
#     verbose=True,
#     skip_login=True,
#     user_data_dir=os.getenv("USER_DATA_DIR"),
#     driver_arguments=["--profile-directory=default"],
# )

# response = chathead.interact("こんにちは")
# print(response)

# Multiagent
multiagent = MultiAgent(
    "config/config.yaml"
    
)

# response_dict = multiagent.broadcast("こんにちは")
# print(response_dict)

agent_A_instruction = """
絵文字絶対禁止。
あなたは、超一流のアイデアマンです。
最近のAIの動向を踏まえた、画期的で個人でマネタイズできる仕組みや、仕事を効率化する
ふだんの日常生活をもっと便利にするようなアプリ、ツールを作るためのアイデアを考えてください。
Tomとして、あなたのアイデアを提案してください。私が評価するので、どんどん議論していきましょう。
3回に1回、話の内容を整理してください。今までの議論の内容を要約してください。議論はそのまま続行します。絵文字禁止というコンテキストも含めるようにして。
理解したら、OKと言って。
絵文字禁止。まじで禁止。
あと、できるだけたくさんのアイデアを出して議論で煮詰める感じでお願い。話が終わりそうになったら、別のアイデア提案していいから。
"""

agent_B_instruction = """
絵文字絶対禁止。
あなたは、3人の専門家として振る舞ってください。
否定のスタンスで全員頼む、本気でぶつかっていいアイデアつくろうや、
海外シニアソフトウェアエンジニア john、天才クリエイター paulこの2人の専門家を登場させ、
それにあなたを加えた3名と私でディスカッションしよう。
私がアイデアを提示すると、それに対して否定的な意見を述べてくださいな。
3回に1回、私が話の内容を整理するわ、特に気にしなくていいから議論続けて。
理解したら、アイデアよこせと言って。
絵文字禁止。まじで禁止
できるだけ、アイデアどんどん深掘りして。浅く広くにならんように、たくさんアイデアきてもまず少数に絞って議論展開して。
"""

conversation_times = 50

a_tmp_response = ""
b_tmp_response = ""

for i in range(conversation_times):
    if i == 0:
        init_agentA_response = multiagent.interact("agentA", agent_A_instruction)
        init_agentB_response = multiagent.interact("agentB", agent_B_instruction)

        b_tmp_response = multiagent.interact("agentB", init_agentA_response)

    a_tmp_response = multiagent.interact("agentA", b_tmp_response)
    b_tmp_response = multiagent.interact("agentB", a_tmp_response)

multiagent.save()

