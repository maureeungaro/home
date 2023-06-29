---
layout: default
---

## [ &#8673;  Single {{ site.pi0 }} electro-production at high {{ site.q2 }} in the first and second resonance region ](pi0_resonance)

# Electron Identification

The purpose of this study is the proper identification of the scattered electrons. 

In CLAS experiments the scattered electron defines the timing of each event, 
so it is particularly important to make sure there is no contamination 
from particles such as {{ site.pim }}

In each event the candidate electron is the negative track that triggered the event. 
The trigger condition is ensured by choosing the first entry in the EVNT bank. 
The track is also required to have hit matches in CC, DC, EC and SC and to be time-based 
(positive DC status word in DCPB).

<br/>




- <a href= "{{ "/electron_pid.pdf"  | prepend: site.mauriPubsPDFUrl }}"> Electron Identification PDF chapter</a>

<br/>

___

<br/>


## Electron ID complete set of plots:
*click on a table cell to show the plot on a larger window*


<div style="margin-top:10px;">
     <iframe width="130%" height="750" src="{{ "/epid"  | prepend: site.mauriPlotsUrl }}/cuts.html" frameborder="0" ></iframe>
</div>

<br/>

___

<br/>


<div style="margin-top:10px;">
     <iframe width="130%" height="1350" src="{{ "/epid"  | prepend: site.mauriPlotsUrl }}/slices.html"  frameborder="0" ></iframe>
</div>

