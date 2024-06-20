import os,sys
import os.path as osp

import cv2
import numpy as np
import matplotlib.pyplot as plt
import json
from collections import deque

fn_img = 'kun.bmp'
im = cv2.imread(fn_img)
im[im<=100] = 0
im[im>100] = 1
im = im[..., 0]
plt.imshow(im)

h,w = im.shape[:2]


dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

visited = im.copy()
visited[:] = 0

path = []

def dfs(y, x): # this bfs will likely get stack overflow error
    print(visited.sum() / 45559)
    path.append((y,x))
    visited[y, x] = 1
    for dy, dx in dirs:
        ny,nx = y+dy, x+dx
        if 0<=ny<h and 0<=nx<w and not visited[ny, nx] and im[ny, nx] == 0:
            dfs(ny, nx)
        path.append((y,x))

path.append((h-1, 0))

queue = deque()
queue.append((h-1, 0))
while(queue): # dfs w/o recursion
    #print((visited>0).sum() / 45559)
    y,x = queue.popleft()
    if path[-1] != (y,x):
        path.append((y,x))
    d = visited[y,x]
    if d <= 3:
        queue.appendleft((y, x))
        dy,dx = dirs[d]
        visited[y,x] += 1
        ny,nx = y+dy, x+dx
        if 0<=ny<h and 0<=nx<w and not visited[ny, nx] and im[ny, nx] == 0:
            queue.appendleft((ny, nx))
        
print('path len:', len(path))
        
npath = [list(path[0]), list(path[0])]
for step in path:
    if step[0] != npath[-1][0] or step[0] != npath[-2][0]:
        npath.append(list(step))
    else:
        if (npath[-1][1] - npath[-2][1]) * (step[1] - npath[-1][1]) > 0:
            npath[-1][1] = step[1]
        else:
            npath.append(list(step))
            
print('npath len:', len(npath))

# coordinate convert
# im.shape = (387, 640)
# sketch.shape = (4000, 6500)


steps = []
for y,x in npath:
    y = im.shape[0]-y
    steps.append(x*9)
    steps.append(y*9)
    
#print(','.join(str(i) for i in steps))

with open(fn_img+'.json', 'w') as f:
    json.dump(steps, f)

 