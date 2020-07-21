from summarizer import Summarizer

s2 = 'updated may wednesday condemned misogynistic comments made washington capitals forward brendan leipsic florida ' \
   'panthers prospect jack rodewald group chat social media comments included vulgar disparagement girlfriends wives ' \
   'players chat also described sexual conquests graphic terms included discussion cocaine use place league statements' \
   ' attitudes behavior matter form said statement address inexcusable conduct clubs players involved leipsic fourth ' \
   'season apologized wednesday comments said statement recognized inappropriate offensive comments capitals released ' \
   'statement several news media organizations saying would deal matter internally instagram group chat messages posted' \
   ' hacked leipsic said images conversation posted social media accounts said participants believed chat private ' \
   'committed learning becoming better person taking time determine move forward accountable meaningful way leipsic ' \
   'said truly sorry rodewald games experience ottawa senators played panthers minor league system season second incident ' \
   'offensive behavior condemned league spring involved racist remarks someone hacked videoconference featuring rangers' \
   ' prospect andre miller identifies african american string racial slurs scrolled across screen several seconds live ' \
   'chat rangers shut team league criticized anticipating trouble videoconference platform zoom repeatedly target ' \
   'offensive hacks advertisementcontinue reading main storysite indexsite information navigation new york times ' \


model = Summarizer()
result = model(s2, min_length=60)
full = ''.join(result)
print(full)