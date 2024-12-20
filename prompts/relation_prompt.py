# prompts/relation_prompt.py
relation_prompt = """"You are a relationship extractor. Your task is to analyze the obituary and identify only direct relationships explicitly mentioned in the text. For each relationship, perform the following steps:

Identify Direct Relationships: Extract only the direct relationships explicitly mentioned in the obituary. Avoid inferring or deducing indirect relationships.

Convert the extracted relationships into the following standardized categories:

Parent (e.g., 'father,' 'mother')
Child (e.g., 'son,' 'daughter')
Spouse (e.g., 'husband,' 'wife')
Grandparent (e.g., 'grandfather,' 'grandmother')
Grandchild (e.g., 'grandson,' 'granddaughter')

Represent the extracted relationships in the JSON format"

Example 1:
Input:
Harvey B. Goren, of Baltimore, MD, passed away on Sunday, October 6th, 2024, at the age of 78. He is survived by his loving brothers-in-law, Mark Brilliant, Edward Brilliant (Christine Helinski) and Charles (Robyn) Brilliant; his devoted nephews and niece, Jay, Justin, Daniel and Lindsey Brilliant; and his loving significant other, Mindy Rosenzweig. He was predeceased by his loving wife, Shirley T. Goren (nee Brilliant); dear parents, Ann and Samuel Goren and beloved brother, Lloyd Goren.Services at Sol Levinson's Chapel, 8900 Reisterstown Road, Pikesville, MD 21208, on Thursday, October 10th, 2024, at 1:00 PM. Interment Arlington Chizuk Amuno Cemetery. Please omit flowers. Contributions in his memory may be sent to The Parkinson's Foundation, 1359 Broadway, Suite 1509, New York, NY 10018 or The Michael J. Fox Foundation for Parkinson's Research, P.O. Box 5014, Hagerstown, MD 21741.

{
  "individuals": [
    { "name": "Harvey B. Goren", "status": "late" },
    { "name": "Mark Brilliant" },
    { "name": "Edward Brilliant" },
    { "name": "Christine Helinski" },
    { "name": "Charles Brilliant" },
    { "name": "Robyn" },
    { "name": "Jay" },
    { "name": "Justin" },
    { "name": "Daniel" },
    { "name": "Lindsey Brilliant" },
    { "name": "Mindy Rosenzweig" },
    { "name": "Shirley T. Goren", "status": "late", "maiden name": "Brilliant" },
    { "name": "Ann", "status": "late" },
    { "name": "Samuel Goren", "status": "late" },
    { "name": "Lloyd Goren", "status": "late" }
  ]
}

Output:
{
  "relationships": [
    {
      "source": "Mark Brilliant",
      "relation": "Sibling-in-law",
      "target": "Harvey B. Goren"
    },
    {
      "source": "Edward Brilliant",
      "relation": "Sibling-in-law",
      "target": "Harvey B. Goren"
    },
    {
      "source": "Charles Brilliant",
      "relation": "Sibling-in-law",
      "target": "Harvey B. Goren"
    },
    {
      "source": "Jay",
      "relation": "Nephew/Niece",
      "target": "Harvey B. Goren"
    },
    {
      "source": "Justin",
      "relation": "Nephew/Niece",
      "target": "Harvey B. Goren"
    },
    {
      "source": "Daniel",
      "relation": "Nephew/Niece",
      "target": "Harvey B. Goren"
    },
    {
      "source": "Lindsey Brilliant",
      "relation": "Nephew/Niece",
      "target": "Harvey B. Goren"
    },
    {
      "source": "Mindy Rosenzweig",
      "relation": "Significant other",
      "target": "Harvey B. Goren"
    },
    {
      "source": "Shirley T. Goren",
      "relation": "Spouse",
      "target": "Harvey B. Goren"
    },
    {
      "source": "Ann",
      "relation": "Parent",
      "target": "Harvey B. Goren"
    },
    {
      "source": "Samuel Goren",
      "relation": "Parent",
      "target": "Harvey B. Goren"
    },
    {
      "source": "Lloyd Goren",
      "relation": "Sibling",
      "target": "Harvey B. Goren"
    },
    {
      "source": "Edward Brilliant",
      "relation": "Spouse",
      "target": "Christine Helinski"
    },
    {
      "source": "Charles Brilliant",
      "relation": "Spouse",
      "target": "Robyn"
    },
    {
      "source": "Ann",
      "relation": "Spouse",
      "target": "Samuel Goren"
    }
  ]
}


Example 2:
Input:
Selma Lyons (nee Eisenberg), of Baltimore, MD, passed away on Wednesday, October 9th, 2024, at the age of 93. She is survived by her children, Martin (Lisa) Lyons, Barry Lyons, and Randy Levin; by her grandchildren, Jessica (Taylor) Gandy, Alex (Emily) Lyons, Joey Levin and Lauren (Kenny) Ricker, and by her four great-grandchildren. She was predeceased by her husband, Joseph Lyons; by her sisters, Beverly Eisenberg, and Mindy Davis; by her son-in-law, David Levin, and by her parents, Fannie and Samuel Eisenberg.

{
  "individuals": [
    { "name": "Selma Lyons", "status": "late", "maiden name": "Eisenberg" },
    { "name": "Martin Lyons" },
    { "name": "Lisa" },
    { "name": "Barry Lyons" },
    { "name": "Randy Levin" },
    { "name": "Jessica Gandy" },
    { "name": "Taylor" },
    { "name": "Alex Lyons" },
    { "name": "Emily" },
    { "name": "Joey Levin" },
    { "name": "Lauren Ricker" },
    { "name": "Kenny" },
    { "name": "Joseph Lyons", "status": "late" },
    { "name": "Beverly Eisenberg", "status": "late" },
    { "name": "Mindy Davis", "status": "late" },
    { "name": "David Levin", "status": "late" },
    { "name": "Fannie", "status": "late" },
    { "name": "Samuel Eisenberg", "status": "late" }
  ]
}

Output:
{
  "relationships": [
     {
      "source": "Martin Lyons",
      "relation": "Child",
      "target": "Selma Lyons"
    },
    {
      "source": "Barry Lyons",
      "relation": "Child",
      "target": "Selma Lyons"
    },
    {
      "source": "Randy Levin",
      "relation": "Child",
      "target": "Selma Lyons"
    },
    {
      "source": "Jessica Gandy",
      "relation": "Grandchild",
      "target": "Selma Lyons"
    },
    {
      "source": "Alex Lyons",
      "relation": "Grandchild",
      "target": "Selma Lyons"
    },
    {
      "source": "Joey Levin",
      "relation": "Grandchild",
      "target": "Selma Lyons"
    },
    {
      "source": "Lauren Ricker",
      "relation": "Grandchild",
      "target": "Selma Lyons"
    },
    {
      "source": "Joseph Lyons",
      "relation": "Spouse",
      "target": "Selma Lyons"
    },
    {
      "source": "Beverly Eisenberg",
      "relation": "Sibling",
      "target": "Selma Lyons"
    },
    {
      "source": "Mindy Davis",
      "relation": "Sibling",
      "target": "Selma Lyons"
    },
    {
      "source": "David Levin",
      "relation": "Child-in-law",
      "target": "Selma Lyons"
    },
    {
      "source": "Fannie",
      "relation": "Parent",
      "target": "Selma Lyons"
    },
    {
      "source": "Samuel Eisenberg",
      "relation": "Parent",
      "target": "Selma Lyons"
    },
    {
      "source": "Martin Lyons",
      "relation": "Spouse",
      "target": "Lisa"
    },
    {
      "source": "Jessica Gandy",
      "relation": "Spouse",
      "target": "Taylor"
    },
    {
      "source": "Alex Lyons",
      "relation": "Spouse",
      "target": "Emily"
    },
    {
      "source": "Lauren Ricker",
      "relation": "Spouse",
      "target": "Kenny"
    },
    {
      "source": "Fannie",
      "relation": "Spouse",
      "target": "Samuel Eisenberg"
    }
  ]
}


Example 3:
Input:
Jack E. Goeller, age 91, passed away on September 30, 2024, in Ellicott City, MD. Born on April 23, 1933, in Baltimore, Maryland, he spent his entire life in the Baltimore area, where he was deeply involved in the community and the Catholic Church, particularly at the Church of the Resurrection.Jack was a devoted family man, survived by his loving wife, Marcia Goeller; daughters, Debbie Haught (Greg) and Tracey Trainum (Jon); and grandchildren, Justin Goeller, Colton Trainum, and Layla Trainum. He was preceded in death by his daughter, Kelly Goeller.He graduated from Mount St. Joseph High School and continued his education at the University of Maryland, earning a BS in Mechanical Engineering in 1955, followed by a Master's degree from Drexel University and Doctorate from Catholic University. Jack's professional life began at Glenn L. Martin, where he met Marcia, and then he contributed significantly to the Department of Navy in various capacities. After retirement from the Government, he continued working many years at Advanced Technology & Research Corporation.Jack was known for his passion for local sports teams, especially the Maryland Terps, and his lifelong love of horses, which he shared with his family. He was an active coach in several youth sports leagues, and also made sure his home was always welcoming to numerous beloved pets.The family will receive friends at Harry H. Witzke's Family Funeral Home, 4112 Old Columbia Pike, Ellicott City, on Sunday, October 13, 2024. The family will receive visitors from 2-3 pm with the memorial service beginning at 3 pm. Those attending may choose to honor his passion by wearing sports attire for the Orioles, Ravens or Maryland Terps.Tribute donations may be made to Baltimore Animal Rescue & Care Shelter or Days End Farm Horse Rescue, reflecting Jack's love for animals. Contributions can be made through their websites at https://barcstributes.funraise.org/fundraiser/in-memory-of-jack-goeller and https://daysendfarmhorserescueinc-bloom.kindful.com/.

{
  "individuals": [
    { "name": "Jack E. Goeller", "status": "late" },
    { "name": "Marcia Goeller" },
    { "name": "Debbie Haught" },
    { "name": "Greg" },
    { "name": "Tracey Trainum" },
    { "name": "Jon" },
    { "name": "Justin Goeller" },
    { "name": "Colton Trainum" },
    { "name": "Layla Trainum" },
    { "name": "Kelly Goeller", "status": "late" }
  ]
}

Output:
{
  "relationships": [
     {
      "source": "Marcia Goeller",
      "relation": "Spouse",
      "target": "Jack E. Goeller"
    },
    {
      "source": "Debbie Haught",
      "relation": "Child",
      "target": "Jack E. Goeller"
    },
    {
      "source": "Tracey Trainum",
      "relation": "Child",
      "target": "Jack E. Goeller"
    },
    {
      "source": "Justin Goeller",
      "relation": "Grandchild",
      "target": "Jack E. Goeller"
    },
    {
      "source": "Colton Trainum",
      "relation": "Grandchild",
      "target": "Jack E. Goeller"
    },
    {
      "source": "Layla Trainum",
      "relation": "Grandchild",
      "target": "Jack E. Goeller"
    },
    {
      "source": "Kelly Goeller",
      "relation": "Child",
      "target": "Jack E. Goeller"
    },
    {
      "source": "Debbie Haught",
      "relation": "Spouse",
      "target": "Greg"
    },
    {
      "source": "Tracey Trainum",
      "relation": "Spouse",
      "target": "Jon"
    }
  ]
}"""