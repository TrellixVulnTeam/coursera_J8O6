function factorList = constructGeneticNetwork(pedigree, alleleFreqs, alphaList)

% This function constructs a Bayesian network for genetic
% inheritance. It assumes that there are only 2 phenotypes.  It also
% assumes that either both parents are specified or neither parent is
% specified.
%
% In Matlab, each variable will have a number.  We need a consistent
% way of numbering variables when instantiating CPDs so that we know
% what variables are involved in each CPD.  For example, if
% IraGenotype is in multiple CPDs and IraGenotype is number variable 1
% in a CPD, then IraGenotype should be numbered as variable 1 in all
% CPDs and no other variables should be numbered 1; thus, every time
% variable 1 appears in our network, we will know that it refers to
% Ira's genotype.
%
% Here is how the variables should be numbered, for a pedigree with n
% people:
%
% 1.  The first n variables should be the genotype variables and
% should be numbered according to the index of the corresponding
% person in pedigree.names; the ith person with name pedigree.names{i}
% has genotype variable number i.
%
% 2.  The next n variables should be the phenotype variables and
% should be numbered according to the index of the corresponding
% person in pedigree.names; the ith person with name pedigree.names{i}
% has phenotype variable number n+i.
%
% Here is an example of how the variable numbering should work: if
% pedigree.names = {'Ira', 'James', 'Robin'} and pedigree.parents =
% [0, 0; 1, 3; 0, 0], then the variable numbering is as follows:
%
% Variable 1: IraGenotype
% Variable 2: JamesGenotype
% Variable 3: RobinGenotype
% Variable 4: IraPhenotype
% Variable 5: JamesPhenotype
% Variable 6: RobinPhenotype
%
% Input:
%
%   pedigree: Data structure that includes names, genders, and
%   parent-child relationships
%
%   alleleFreqs: Frequencies of alleles in the population
%   alphaList: m x 1 vector of alpha values for genotypes, where m is
%   the number of genotypes -- the alpha value for a genotype is the
%   probability that a person with that genotype will have the
%   physical trait
%
% Output: factorList: Struct array of factors for the genetic network
%   (In each factor, .var, .card, and .val are all row 1-D vectors.)

numPeople = length(pedigree.names);
numAlleles = length(alleleFreqs); % Number of alleles

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%INSERT YOUR CODE HERE
% Variable numbers:
% 1 - numPeople: genotype variables
% numPeople+1 - 2*numPeople: phenotype variables
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

factorList(2*numPeople) = struct('var', [], 'card', [], 'val', []);
for i=1:numPeople
  if (pedigree.parents(i) == [0, 0])
    factorList(i) = genotypeGivenAlleleFreqsFactor(
                        alleleFreqs,
                        i);
  else
    factorList(i) = genotypeGivenParentsGenotypesFactor(
                        numAlleles,
                        i,
                        pedigree.parents(i, 1),
                        pedigree.parents(i, 2));
  end
end

for i=1:numPeople
  factorList(numPeople + i) = phenotypeGivenGenotypeFactor(
                      alphaList,
                      i,
                      numPeople + i);
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
