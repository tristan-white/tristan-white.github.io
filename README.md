# Build locally

```bash
sudo apt install rbenv
rbenv install --list # pick one
rbenv intall 3.1.2
rbenv global 3.1.2
rbenv exec gem install system
rbenv exec gems install bundler
rbenv exec bundle install
rbenv exec bundle exec jekyll serve
```
