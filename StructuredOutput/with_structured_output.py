from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY")
)


class Review(TypedDict):
    key_themes: Annotated[
        list[str], "Write down all the key things discussed int he review in the list"
    ]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[
        Literal["pos","neg"], "Return sentiment of the review either negative,posetive or neutral"
    ]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name:Annotated[str,"Write the name of the reviewer"]


structured_model = model.with_structured_output(Review)


result = structured_model.invoke(
    """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don’t use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

Pros
Insanely Powerful Processor: The Snapdragon 8 Gen 3 handles gaming, multitasking, and photo editing with lightning-fast performance.

Exceptional Battery & Charging: Features a long-lasting 5000mAh battery for full-day heavy use, backed by a 45W fast charging lifesaver.

Stunning 200MP Camera: Features an incredible night mode for crisp, vibrant low-light images and impressive zoom capabilities.

S-Pen Integration: Provides a handy tool for note-taking and quick sketches.

Cons
Bulk and Weight: The physical size and weight make it a bit uncomfortable for one-handed use.

Software Bloatware: One UI includes multiple duplicate Samsung apps for services Google already provides.

High Price Tag: The $1,300 price makes it an expensive investment.

Zoom Quality Dropoff: While zooming up to 100x works well, anything beyond 30x loses noticeable quality.

Review by Sulav Dhami
                    """
)

print(result)
print(result["sentiment"])
