
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled,FetchedTranscriptSnippet

# video_id = "X4FVEEegCbk"
# ytTranscript = YouTubeTranscriptApi()
# try:
#     transcript_list = ytTranscript.fetch(video_id=video_id, languages=["en"])
#     transcript = " ".join(chunk.snippets.text for chunk in transcript_list)
#     print(transcript)
# except TranscriptsDisabled:
#     print("No caption available for this video!")

transcript = [
    FetchedTranscriptSnippet(
        text="There are different ways to give an AI agent the knowledge it needs to",
        start=0.17,
        duration=2.085,
    ),
    FetchedTranscriptSnippet(
        text="complete a task beyond the knowledge that it just has in its training data.",
        start=2.255,
        duration=5.594,
    ),
    FetchedTranscriptSnippet(
        text="So let's look at four of them, skills, MCP, RAG and memory and define which methods are best in different situations.",
        start=7.95,
        duration=10.26,
    ),
    FetchedTranscriptSnippet(
        text="So let us consider that we've got some kind of web app here and we look at this webpage,",
        start=18.41,
        duration=7.603,
    ),
    FetchedTranscriptSnippet(
        text="and uh-oh, this webpage is throwing error the dreaded 500 internal server error.",
        start=26.013,
        duration=9.786,
    ),
    FetchedTranscriptSnippet(
        text="Okay we need to fix this.", start=36.1, duration=2.16
    ),
    FetchedTranscriptSnippet(
        text="Well the goal of an AI agent is to do just that.",
        start=38.4,
        duration=7.019,
    ),
    FetchedTranscriptSnippet(
        text="We want to resolve this error.", start=45.42, duration=2.079
    ),
    FetchedTranscriptSnippet(
        text="Now I think instinctively the answer to getting some agentic help for this 500 error is just to kind of gather as much context as possible?",
        start=48.22,
        duration=10.4,
    ),
    FetchedTranscriptSnippet(
        text="Then throw that into the context window from the actual agent itself.",
        start=59.03,
        duration=6.879,
    ),
    FetchedTranscriptSnippet(
        text="So in this context window we might store a bunch of runbooks and then maybe we'd also pass it a bunch of dashboards",
        start=65.97,
        duration=10.034,
    ),
    FetchedTranscriptSnippet(
        text="and perhaps also we'd have a little bit of customer history in here as well",
        start=76.004,
        duration=5.919,
    ),
    FetchedTranscriptSnippet(
        text="and just throw it in the context window and then let the AI agent figure out how to resolve this error.",
        start=81.923,
        duration=8.187,
    ),
    FetchedTranscriptSnippet(
        text="But that can be quite an ineffective means to resolve an error like,",
        start=90.91,
        duration=4.425,
    ),
    FetchedTranscriptSnippet(
        text="this because there's plenty of scope for this AI agent to kind of get lost or to go down dead ends",
        start=95.335,
        duration=6.409,
    ),
    FetchedTranscriptSnippet(
        text="or just act in a generalized way that doesn't really represent how this specific checkout page actually works.",
        start=101.744,
        duration=7.245,
    ),
    FetchedTranscriptSnippet(
        text="So just throwing context into the fire it might not be the best way to go. Perhaps a better approach would be to use...",
        start=109.33,
        duration=8.86,
    ),
    FetchedTranscriptSnippet(
        text="Skills or MCP or RAG or memory maybe all of the above,",
        start=118.71,
        duration=6.18,
    ),
    FetchedTranscriptSnippet(
        text="but how, well i'm going to take these one at a time as to how we can get this web page resolved with this AI agent",
        start=124.89,
        duration=7.312,
    ),
    FetchedTranscriptSnippet(
        text="and let's start with the first one which is to use agent skills.",
        start=132.202,
        duration=6.906,
    ),
    FetchedTranscriptSnippet(
        text="Now, an agent skill is really just kind of a set of instructions that we can hand to the agent.",
        start=139.108,
        duration=7.762,
    ),
    FetchedTranscriptSnippet(
        text="Doing one particular kind of task.", start=147.57, duration=2.079
    ),
    FetchedTranscriptSnippet(
        text="So sometimes it might also have a bit of code attached as well.",
        start=150.15,
        duration=2.78,
    ),
    FetchedTranscriptSnippet(
        text="Now it might list a procedure, like the steps to follow, along with some judgment about when to follow them,",
        start=153.15,
        duration=6.411,
    ),
    FetchedTranscriptSnippet(
        text="and the agent only pulls the skill in when the task actually calls for it through something called progressive disclosure.",
        start=159.561,
        duration=7.348,
    ),
    FetchedTranscriptSnippet(
        text="So for this checkout error we've got here, we might give the agent a special skill that we have created.",
        start=167.17,
        duration=6.26,
    ),
    FetchedTranscriptSnippet(
        text="Let's call this the triage skill.", start=173.51, duration=3.02
    ),
    FetchedTranscriptSnippet(
        text="And that skill lays out the run book.", start=177.24, duration=2.739
    ),
    FetchedTranscriptSnippet(
        text="So maybe it says, first of all, we need to take a look at the error rate.",
        start=180.26,
        duration=7.14,
    ),
    FetchedTranscriptSnippet(
        text="That's the first thing we need do.", start=187.58, duration=1.16
    ),
    FetchedTranscriptSnippet(
        text="And then once we've done that, the skill says the next thing to do is to check on the status of the recent deployments.",
        start=189.14,
        duration=7.94,
    ),
    FetchedTranscriptSnippet(
        text="So these are the steps to follow.", start=197.8, duration=1.42
    ),
    FetchedTranscriptSnippet(
        text="But beyond the steps, to take, a good skill can also carry a bit of judgment as well.",
        start=199.62,
        duration=5.22,
    ),
    FetchedTranscriptSnippet(
        text="Like, when the agent should stop.", start=204.84, duration=1.539
    ),
    FetchedTranscriptSnippet(
        text="Poking around on its own and instead it should escalate to maybe a actual human to help with the problem.",
        start=206.63,
        duration=7.74,
    ),
    FetchedTranscriptSnippet(
        text="Now without this triage skill the agent probably wouldn't know to do all of these things,",
        start=215.05,
        duration=6.622,
    ),
    FetchedTranscriptSnippet(
        text="because this information is not sitting in the model's training data anywhere,",
        start=221.672,
        duration=5.365,
    ),
    FetchedTranscriptSnippet(
        text="so a skill gives the agent a clear procedure and maybe a bit of judgment about how to run it. But, it kind of stops there.",
        start=227.037,
        duration=8.932,
    ),
    FetchedTranscriptSnippet(
        text="The skill can tell the agent to go and check the the error rate but the agent",
        start=236.13,
        duration=5.141,
    ),
    FetchedTranscriptSnippet(
        text="still can't necessarily reach the dashboard to actually read that error rate in the first place.",
        start=241.271,
        duration=5.468,
    ),
    FetchedTranscriptSnippet(
        text="So one way to deal with getting that error rates and stuff like that is to use MCP, that's the model context protocol.",
        start=247.06,
        duration=9.399,
    ),
    FetchedTranscriptSnippet(
        text="It can connect the agent to the outside world so it can actually go out and do things.",
        start=256.6,
        duration=5.44,
    ),
    FetchedTranscriptSnippet(
        text="Now, the way it works is there is a standard MCP protocol sitting between the agent and whatever it needs to reach.",
        start=262.22,
        duration=8.34,
    ),
    FetchedTranscriptSnippet(
        text="Now the agent itself, that is considered the MCP host and each system it wants to talk to that sits behind an MCP",
        start=270.82,
        duration=11.88,
    ),
    FetchedTranscriptSnippet(text="server.", start=283.54, duration=1.0),
    FetchedTranscriptSnippet(text="So...", start=285.06, duration=0.58),
    FetchedTranscriptSnippet(
        text="This model on its own maybe hasn't got a clue how to say query a particular backend that has a logging stack,",
        start=285.64,
        duration=7.458,
    ),
    FetchedTranscriptSnippet(
        text="but the MCP server for that logging stack does know how to connect to it",
        start=293.098,
        duration=4.903,
    ),
    FetchedTranscriptSnippet(
        text="and it exposes that as something that the agent can then call.",
        start=298.001,
        duration=3.338,
    ),
    FetchedTranscriptSnippet(
        text="So if we go back to my 500 error here, the skill that's said to check the error rate.",
        start=301.96,
        duration=5.999,
    ),
    FetchedTranscriptSnippet(
        text="Well, with MCP, the agent could reach all of that information so it can get hold of all of the",
        start=308.48,
        duration=7.04,
    ),
    FetchedTranscriptSnippet(
        text="logs by performing an MCP call.", start=315.81, duration=2.36
    ),
    FetchedTranscriptSnippet(
        text="It can get hold of the metrics as well by doing the same thing and it can read the error rate for real.",
        start=318.35,
        duration=7.399,
    ),
    FetchedTranscriptSnippet(
        text="Right so getting the error rate is is solved by MCP.",
        start=327.05,
        duration=4.479,
    ),
    FetchedTranscriptSnippet(
        text="We're calling out to another service but what the agent still doesn't know yet",
        start=331.55,
        duration=4.779,
    ),
    FetchedTranscriptSnippet(
        text="is well it doesn't really have any real knowledge of how this particular set up for this webpage behaves",
        start=336.329,
        duration=5.577,
    ),
    FetchedTranscriptSnippet(
        text="like what's normal or what the dependencies are and what's maybe caused some of these issues before.",
        start=341.906,
        duration=6.233,
    ),
    FetchedTranscriptSnippet(
        text="So where does that knowledge come from?", start=349.5, duration=1.439
    ),
    FetchedTranscriptSnippet(
        text="Well, you probably guessed it.", start=351.54, duration=1.44
    ),
    FetchedTranscriptSnippet(
        text="It comes from the other two things on my list here.",
        start=353.08,
        duration=2.379,
    ),
    FetchedTranscriptSnippet(
        text="So let's start with RAG.", start=355.82, duration=2.0
    ),
    FetchedTranscriptSnippet(text="This is", start=358.56, duration=1.0),
    FetchedTranscriptSnippet(
        text="Retrieval Augmented Generation.", start=360.62, duration=2.32
    ),
    FetchedTranscriptSnippet(
        text="And the idea is instead of stuffing everything into the context window up front,",
        start=363.36,
        duration=4.909,
    ),
    FetchedTranscriptSnippet(
        text="the agent is just gonna pull in the information that it needs,",
        start=368.269,
        duration=3.471,
    ),
    FetchedTranscriptSnippet(
        text="some sort of relevant piece of information from some outside source, and to only do it when it actually needs it.",
        start=371.74,
        duration=6.159,
    ),
    FetchedTranscriptSnippet(
        text="So for our checkout error, we might point RAG at a collection of our own documents.",
        start=378.34,
        duration=8.219,
    ),
    FetchedTranscriptSnippet(text="So these might be like", start=386.8, duration=1.0),
    FetchedTranscriptSnippet(
        text="manuals or dependency maps, stuff like that,",
        start=388.02,
        duration=3.372,
    ),
    FetchedTranscriptSnippet(
        text="and then the agent gets to ask its question and then RAG is going to retrieve the matching pieces by",
        start=391.392,
        duration=11.319,
    ),
    FetchedTranscriptSnippet(
        text="performing something called a semantic search and relevant",
        start=402.711,
        duration=4.216,
    ),
    FetchedTranscriptSnippet(
        text="matching chunks then they get returned back to the agent's context window. That's RAG.",
        start=406.927,
        duration=8.633,
    ),
    FetchedTranscriptSnippet(text="And then...", start=416.42, duration=1.039),
    FetchedTranscriptSnippet(
        text="The last one to talk about is talking about memory.",
        start=417.62,
        duration=5.8,
    ),
    FetchedTranscriptSnippet(
        text="And memory at first glance sounds quite a bit like RAG,",
        start=423.91,
        duration=3.937,
    ),
    FetchedTranscriptSnippet(
        text="where the agent pulls in relevant pieces of knowledge when it's needed, but there is a difference between these two things.",
        start=427.847,
        duration=6.443,
    ),
    FetchedTranscriptSnippet(
        text="And the difference is where the knowledge comes from.",
        start=435.13,
        duration=2.759,
    ),
    FetchedTranscriptSnippet(
        text="So RAG it reads documents which are stored in a vector database.",
        start=438.53,
        duration=4.679,
    ),
    FetchedTranscriptSnippet(
        text="And those documents were put in that vector database by a person, like they were stored there deliberately.",
        start=443.45,
        duration=4.939,
    ),
    FetchedTranscriptSnippet(
        text="But memory is the stuff that the agent has picked up itself and kind of stored",
        start=449.03,
        duration=5.292,
    ),
    FetchedTranscriptSnippet(
        text="for later from things that have happened previously.",
        start=454.322,
        duration=4.148,
    ),
    FetchedTranscriptSnippet(
        text="So the agent can look back at some kind of memory like previous error situations.",
        start=459.03,
        duration=6.659,
    ),
    FetchedTranscriptSnippet(
        text="Maybe last time this exact error happened the real cause was not",
        start=465.93,
        duration=3.785,
    ),
    FetchedTranscriptSnippet(
        text="something that was documented in the the run book over here and it kind of had to get worked out the hard way.",
        start=469.715,
        duration=5.665,
    ),
    FetchedTranscriptSnippet(
        text="Well that memory can tell us what that hard way was.",
        start=475.38,
        duration=3.743,
    ),
    FetchedTranscriptSnippet(
        text="And when this pesky 500 error is finally fixed, then the memory can also write back what the fix actually was.",
        start=479.38,
        duration=9.459,
    ),
    FetchedTranscriptSnippet(
        text="So the agent has that for next time.", start=488.96, duration=2.34
    ),
    FetchedTranscriptSnippet(
        text="So basically experience is building up here in the agentic memory.",
        start=491.76,
        duration=4.379,
    ),
    FetchedTranscriptSnippet(
        text="So that is all four and a rough rule of thumb on when to use each one.",
        start=497.1,
        duration=6.799,
    ),
    FetchedTranscriptSnippet(
        text="Well, if it's knowledge that somebody has written down That's RAG.",
        start=504.34,
        duration=5.9,
    ),
    FetchedTranscriptSnippet(
        text="If it's knowledge the agents picked up from experience, that's memory.",
        start=510.66,
        duration=5.019,
    ),
    FetchedTranscriptSnippet(
        text="If its a procedure to follow something repeatable, that is an agent skill.",
        start=516.28,
        duration=6.079,
    ),
    FetchedTranscriptSnippet(
        text="And if an agent needs to go and actually look something up in the world without using proprietary code, that can be MCP.",
        start=522.78,
        duration=8.779,
    ),
    FetchedTranscriptSnippet(
        text="So tell me, does that reflect how you incorporate knowledge with AI agents?",
        start=532.08,
        duration=4.04,
    ),
    FetchedTranscriptSnippet(
        text="Let me know in the comments.", start=536.94, duration=1.119
    ),
]