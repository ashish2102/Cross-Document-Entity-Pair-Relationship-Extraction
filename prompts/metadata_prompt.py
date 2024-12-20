# prompts/metadata_prompt.py
metadata_prompt = """"You are a  biographical and relational metadata extractor specializing in identifying key details for all individuals mentioned in obituaries. Your task is to extract and provide metadata fields for each person referenced in the obituary, returning the information in JSON format. For each individual, extract the following fields when available:

Name
Birth date
Birth location
Death date 
Death location 
Current living location
If a field is not mentioned, output it as null 

Example 1:
Input:
Harvey B. Goren, of Baltimore, MD, passed away on Sunday, October 6th, 2024, at the age of 78. He is survived by his loving brothers-in-law, Mark Brilliant, Edward Brilliant (Christine Helinski) and Charles (Robyn) Brilliant; his devoted nephews and niece, Jay, Justin, Daniel and Lindsey Brilliant; and his loving significant other, Mindy Rosenzweig. He was predeceased by his loving wife, Shirley T. Goren (nee Brilliant); dear parents, Ann and Samuel Goren and beloved brother, Lloyd Goren. Services at Sol Levinson's Chapel, 8900 Reisterstown Road, Pikesville, MD 21208, on Thursday, October 10th, 2024, at 1:00 PM. Interment Arlington Chizuk Amuno Cemetery. Please omit flowers. Contributions in his memory may be sent to The Parkinson's Foundation, 1359 Broadway, Suite 1509, New York, NY 10018 or The Michael J. Fox Foundation for Parkinson's Research, P.O. Box 5014, Hagerstown, MD 21741.
To plant trees in memory, please visit the Sympathy Store.

Output:
{
  "metadata": [
    {
      "Name": "Harvey B. Goren",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": "October 6, 2024",
      "DeathLocation": "Baltimore, MD",
      "CurrentLivingLocation": "Baltimore, MD"
    },
    {
      "Name": "Shirley T. Goren",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Ann Goren",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Samuel Goren",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Lloyd Goren",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Mindy Rosenzweig",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Mark Brilliant",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Edward Brilliant",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Christine Helinski",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Charles Brilliant",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Robyn Brilliant",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Jay Brilliant",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Justin Brilliant",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Daniel Brilliant",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Lindsey Brilliant",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    }
  ]
}


Example 2:
Input:
Selma Lyons (nee Eisenberg), of Baltimore, MD, passed away on Wednesday, October 9th, 2024, at the age of 93. She is survived by her children, Martin (Lisa) Lyons, Barry Lyons, and Randy Levin; by her grandchildren, Jessica (Taylor) Gandy, Alex (Emily) Lyons, Joey Levin and Lauren (Kenny) Ricker, and by her four great-grandchildren. She was predeceased by her husband, Joseph Lyons; by her sisters, Beverly Eisenberg, and Mindy Davis; by her son-in-law, David Levin, and by her parents, Fannie and Samuel Eisenberg.

Output:
{
  "metadata": [
    {
      "Name": "Selma Lyons",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": "October 9, 2024",
      "DeathLocation": "Baltimore, MD",
      "CurrentLivingLocation": "Baltimore, MD"
    },
    {
      "Name": "Joseph Lyons",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Martin Lyons",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Lisa Lyons",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Barry Lyons",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Randy Levin",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Jessica Gandy",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Taylor Gandy",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Alex Lyons",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Emily Lyons",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Joey Levin",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Lauren Ricker",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Kenny Ricker",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Beverly Eisenberg",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Mindy Davis",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "David Levin",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Fannie Eisenberg",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Samuel Eisenberg",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    }
  ]
}


Example 3:
Input:
Jack E. Goeller, age 91, passed away on September 30, 2024, in Ellicott City, MD. Born on April 23, 1933, in Baltimore, Maryland, he spent his entire life in the Baltimore area, where he was deeply involved in the community and the Catholic Church, particularly at the Church of the Resurrection.Jack was a devoted family man, survived by his loving wife, Marcia Goeller; daughters, Debbie Haught (Greg) and Tracey Trainum (Jon); and grandchildren, Justin Goeller, Colton Trainum, and Layla Trainum. He was preceded in death by his daughter, Kelly Goeller.He graduated from Mount St. Joseph High School and continued his education at the University of Maryland, earning a BS in Mechanical Engineering in 1955, followed by a Master's degree from Drexel University and Doctorate from Catholic University. Jack's professional life began at Glenn L. Martin, where he met Marcia, and then he contributed significantly to the Department of Navy in various capacities. After retirement from the Government, he continued working many years at Advanced Technology & Research Corporation.Jack was known for his passion for local sports teams, especially the Maryland Terps, and his lifelong love of horses, which he shared with his family. He was an active coach in several youth sports leagues, and also made sure his home was always welcoming to numerous beloved pets.The family will receive friends at Harry H. Witzke's Family Funeral Home, 4112 Old Columbia Pike, Ellicott City, on Sunday, October 13, 2024. The family will receive visitors from 2-3 pm with the memorial service beginning at 3 pm. Those attending may choose to honor his passion by wearing sports attire for the Orioles, Ravens or Maryland Terps.Tribute donations may be made to Baltimore Animal Rescue & Care Shelter or Days End Farm Horse Rescue, reflecting Jack's love for animals. Contributions can be made through their websites at https://barcstributes.funraise.org/fundraiser/in-memory-of-jack-goeller and https://daysendfarmhorserescueinc-bloom.kindful.com/.

Output:
{
  "metadata": [
    {
      "Name": "Jack E. Goeller",
      "BirthDate": "April 23, 1933",
      "BirthLocation": "Baltimore, MD",
      "DeathDate": "September 30, 2024",
      "DeathLocation": "Ellicott City, MD",
      "CurrentLivingLocation": "Ellicott City, MD"
    },
    {
      "Name": "Marcia Goeller",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Debbie Haught",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Greg Haught",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Tracey Trainum",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Jon Trainum",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Justin Goeller",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Colton Trainum",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Layla Trainum",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    },
    {
      "Name": "Kelly Goeller",
      "BirthDate": null,
      "BirthLocation": null,
      "DeathDate": null,
      "DeathLocation": null,
      "CurrentLivingLocation": null
    }
  ]
}"""
