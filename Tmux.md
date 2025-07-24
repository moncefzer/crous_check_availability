## Use Tmux:

Create Tmux session and start training

```bash
$ tmux new -s crous
$ conda activate crous-scrap
$ cd src
$ python experiments
```

Ctrl+B then D to detach from the session

To re-attach to the training session

```bash
$ tmux a -t crous
```

To kill the session

```bash
$ tmux kill-session -t crous
```
