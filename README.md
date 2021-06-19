# dianthus
  
## Docker

### Version
  
```bash
> docker --version
Docker version 19.03.12, build 48a66213fe

> docker-compose -version
docker-compose version 1.27.2, build 18f557f9
```
  
### Build
  
```bash
> docker-compose up --build -d
```
  
### Run
  
```bash
> docker-compose exec app python main.py
```
  
### Usage
  
```bash
> docker-compose exec app python main.py --help
usage: main.py [-h] [--gen] [--vow] [--demo]

optional arguments:
  -h, --help  show this help message and exit
  --gen       generate csv on ./csv/
  --vow       add column vowel to ./csv/original.csv (create new .csv)
  --demo      return words with the same vowel
```
  


### Test
  
```bash
> docker-compose exec app python -m unittest discover -s ./tests
```