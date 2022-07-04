activate base command

```bash
source activate base
```

create environment

```bash
conda create -n winedata python=3.7 -y
```

activate environment

```bash
conda activate winedata
```

create requirement.txt file

```bash
touch requirements.txt
```

run the requirements.txt

```bash
pip install -r requirements.txt
```

create README file

```bash
touch README.md
```

```bash
git init
```
```bash
dvc init
```
```bash
dvc add data_given/winequality_red.csv
```

```bash
git add .
```

```bash
git commit -m "first commit"
```

```bash
     git add . && git commit -m "updated README file"
```