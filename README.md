# vietnamese-stopwords

A relatively big list of vietnamese stopwords

## How we created it

 1. Scourge the interwebs for all existing lists. Compile them into a list of stopwords. (Not redistributed in this repo)
 2. Scourge the interwebs for all existing words. (Not redistributed in this repo)
 3. Automatically infer a list of potential new stopwords using this algorithm

        potential_stopwords = (stopwords*stopwords) & wordlist (the set operations)

 4. Let a human native speaker plow through the [generated list](https://gist.github.com/Tarrasch/d437e341dc045da5bc445c451858fb3f) and filter to only [real stopwords](https://gist.github.com/qdoan/d289777f854858140e9bff28101f4c19).
 5. Reconcatenate all stopwords and publish on GitHub, letting people using it for greater good! :)

## Who created it

Various employees at VNG Corporation
