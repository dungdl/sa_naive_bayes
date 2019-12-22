from train_attribute import AttributeLabel
from train_entity import EntityLabel
from train_polarity import PolarLabel
from Model import Model



entLabel = EntityLabel("train.json")
entLabel.train()

model2 = Model(entLabel.classifiers, "ent")
model2.save()

attrLabel = AttributeLabel("train.json")
attrLabel.train()

model1 = Model(attrLabel.classifiers, "attr")
model1.save()

polLabel = PolarLabel("train.json")
polLabel.train()

model3 = Model(polLabel.classifiers, "pol")
model3.save()