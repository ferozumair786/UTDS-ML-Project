# Juglone-Resistance
  Updated 1 minute ago    
  
  For this project, we will looked at data from fallingfruit.org for the Austin area and try and find edible plant species that are resistant to Juglone, the major compound in leaves from the Juglanacae (Walnut) family. Walnut, pecan and hickory trees contain a compound called Juglone that is shed onto other plants in the fall. This kills many plants and allows their own saplings to thrive.  
  
  In order to tackle this question, we first needed to figure out which plants grow in close proximity to Pecan and Walnut trees. According to our research, the area of effect for Juglone toxicity is a 50ft radius on average. This is typically how far the trees expand out and disperse leaves in the fall. So we first took all the data from fallingfruit and then only selected data from Austin, TX by limiting the scope of geocodes. 
  
  We then used a crossjoin to merge the two tables so that every plant in the dataset was paired up with a Pecan or Walnut tree. We used this join to line up the coordinates of the Pecans and non Pecans to calculate the Haversine distance between each of those so that we can classify plant species that are growing in close proximity to Pecan and Walnut trees. 
  
  Then, we assigned the plants within 50ft of a Pecan or Walnut tree to a survival value of 1 while all others received a survival value of 0. This way we can train the model based on two features: the species of the plant and the distance from a Pecan or Walnut tree.  What we are trying to predict based on this is whether or not some species of plants are more likely to be found growing underneath these trees because they are resistant to Juglone. 
  
  We used a pipeline with logistic regression for our model, and what we found was very interesting. When we trained separate models for Pecans and Walnuts, we found that Honey Mesquite (Prosopis glandulosa) trees are more frequently found around Walnut trees. However when we trained the model with the Pecan dataset or combined dataset we found that all the plant species were more likely to be distributed evenly across Austin and therefore might not actually be resistant to Juglone. 
  
  This was a very interesting project and we are looking for feedback. We have some ideas to change the scope of the project and pivot it so that we can find other insights using the same data. 
  
  More information on Juglone: https://en.wikipedia.org/wiki/Juglone  
  
  Morton Arboretum from Chicago has an extensive list of Juglone tolerant plants: https://hort.extension.wisc.edu/articles/black-walnut-toxicity/  
  
  App: https://juglone-resistance.herokuapp.com/

