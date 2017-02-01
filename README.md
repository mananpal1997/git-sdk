# git-sdk
Github API SDK for Python

Run ```python setup.py install``` to install

## Use

```
from git_sdk import Github
x = Github("mananpal1997", "************")
# get notifications
x.notifications.get()
# create an issue
x.repos('mananpal1997')('git_sdk').issues.post(title='testing', body='testing')
```

## TODO
  - [ ] Make a doc of easy-to-use commands, from https://developer.github.com/v3/
