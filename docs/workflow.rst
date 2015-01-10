========
Workflow
========

```
Input msg -> class Input():
                  * parse
                  * intention
                        - wants date
                        - wants confirmation
                        - asking question
                        - just trolling
                        - anthing else
                  * save tweet in db

              class Response():
                  * fetch suitable answer from db
                  * update input tuit with ansered status
                  * save response in db
```
