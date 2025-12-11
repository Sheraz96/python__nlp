from collections import Counter
import re
import spacy


nlp = spacy.load("en_core_web_sm")


def keyword_frequency(paragraph, keywords):
    doc = nlp(paragraph.lower())

    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    lemmatized_tokens = [token.lemma_ for token in doc]

    combined_phrases = noun_chunks + lemmatized_tokens


    keyword_counts = {keyword: 0 for keyword in keywords}
    for keyword in keywords:
        for phrase in combined_phrases:
            if keyword in phrase:
                keyword_counts[keyword] += 1

    return keyword_counts


paragraph = """
"Disruption via Garbage Data in communication channels is a sophisticated form of cyberattack where external attackers deliberately flood systems with an overwhelming volume of nonsensical or superfluous data. This tactic, essentially a Denial of Service (DoS) attack, is designed to overburden the processing systems, rendering them incapable of performing their regular functions efficiently. The attack targets critical aspects of functionality that depend on data processing or network communication, such as navigation systems, communication interfaces, and operational controls. By inundating these systems with excessive and meaningless data, attackers aim to disrupt normal operation, leading to degraded service quality, reduced responsiveness, or in severe cases, a total shutdown of vital vehicle functions.
The primary method employed in this attack is resource flooding combined with network disruption techniques, which are designed to exploit the limitations in the data processing capacity. The intent is to create a scenario where systems are so preoccupied with handling the influx of irrelevant data that they fail to process legitimate operational information correctly. The potential impacts of such an attack are significant, ranging from minor inconveniences in functionality to serious safety risks if critical systems are impaired.
To effectively counter this threat, a multi-faceted approach is necessary. This includes the implementation of DoS protection mechanisms capable of identifying and filtering out the surge of unnecessary data.
This is based on UN R155 - Annex 5 - Table A1 - 4.3.2-8-8.1

This vulnerability highlights the risk when vehicle hardware components are compromised, either engineered intentionally to facilitate an attack or due to a failure to meet rigorous design criteria necessary for repelling attacks. Such components can serve as a gateway for cyber attackers to exploit vehicle systems, potentially allowing unauthorized access, control, or the disruption of vehicle functions. Ensuring that all parts meet stringent security standards is vital to protect against such vulnerabilities and maintain vehicle integrity and passenger safety.
This is based on UN R155 - Annex 5 - Table A1 - 4.3.7-27-27.1

Physical access to electronic hardware can create a gateway for cyber attacks. Unauthorized additions or modifications to a vehicle's electronic systems - such as replacing authorized hardware with compromised hardware or manipulating inputs with external devices like magnets- can severely compromise the  operational integrity. These manipulations can alter the data, leading to incorrect responses or unauthorized control. Preventing such attacks requires stringent physical security measures, regular inspections to detect hardware tampering, and secure authentication protocols to ensure the legitimacy of all installed hardware components.
This is based on UN R155 - Annex 5 - Table A1 - 4.3.7-32-32.1"



"""

keywords = ["systems", "attacker", "data", "hardware", "attack"]

result = keyword_frequency(paragraph, keywords)

print("Keyword Frequency:")
for keyword, count in result.items():
    print(f"{keyword}: {count}")


import matplotlib.pyplot as plt

plt.bar(result.keys(), result.values(), color='skyblue')
plt.title('Keyword Frequency')
plt.xlabel('Keywords')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
