# tdmcli
![preview](https://github.com/LukasDrsman/tdmcli/blob/master/preview.png)
<br/>
## Installation
#### Requirements:
* python3

#### Install and run:
```sh
git clone https://github.com/LukasDrsman/tdmcli.git
cd tdmcli
# edit and rename config-example.py to config.py
sudo ./install
tdmcli
```
## Usage
```
▶ [short or long] [arguments]
```
| long        | short           | description  | arguments |
| ------------- |:-------------:| -----|-----------:|
|new       |n       |creates new task         |text| |
|clear     |cl      |clears todolist          | | |
|remove    |rm      |removes task             |task number| |
|load      |l       |loads different todolist | |
|write     |w       |saves todolist           | |
|quit      |q       |exits program            | |
|exit      |x       |exits program            | |
|date      |d       |sets deadline            |task number|
|sort      |s       |sorts todolist           |sorting parameters|
|\*check     |\*cc      |marks task as done       |task number|
|\*uncheck   |\*uc      |marks task as not done   |task number|
|\*important |\*i       |marks task as important  |task number|


\* - can be modified by user

#### Sorting:
```
▶ s [sort by] [order]
```
| sort by (long)| sort by (short) | description  |
| ------------- |:---------------:| -------------:|
|date           |d                |sorts by tasks assigned deadline   |
|priority       |p                |sorts by priority index of tasks' flags  |

| order (long)        | order (short)           | description  |
| ------------- |:-------------:| ----------------:|
|highest       |h       |descending order       |
|lowest        |l       |ascending order        |

<br>

## Todo file

#### Format:

```
task::flag::date
task::flag
```
* task - task to do
* flag - defines the state of the task
* date - optional, format: ```Y-m-d-H-M```
* :: - delimiter

#### Example (using default config):
this:
```
new task::n
task with date::n::2020-6-19-13-35
important task::i
done::d
```
willl render as: <br>
![preview](https://github.com/LukasDrsman/tdmcli/blob/master/preview.png)
