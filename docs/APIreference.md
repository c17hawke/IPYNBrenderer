# API reference

## Rendering Youtube videos

??? note "example"
    ### Short example
    ```python
    from IPYNBrenderer import render_YouTube_video
    URL = "https://youtu.be/roO5VGxOw2s"
    render_YouTube_video(URL=URL, width = 780, height = 480)
    ```

| Args   | Type | Description | 
|:--------:|:------:|:-------|
| URL    | str |input URL of a youtube video as a string |
| height | int |height of the video to display in jupyter notebook, defaults to 720 |
| width  | int |width of the video to display in jupyter notebook, defaults to 600 | 

| Returns   |Type | Description | 
|:--------:|:--------:|:-----|
| Response    |  str   | "success" or InvalidURLException       |


## Rendering reference website

??? note "example"
    ### Short example
    ```python
    from IPYNBrenderer import render_site
    URL = "http://pytorch.org/"
    render_site(URL = URL, width = "90%", height = "500")
    ```

| Args   | Type | Description | 
|:--------:|:------:|:-------|
| URL    | str |input URL of a youtube video as a string |
| height | str |height of the website to display in jupyter notebook, defaults to "600" |
| width  | str |width of the website to display in jupyter notebook, defaults to "100%" | 

| Returns   |Type | Description | 
|:--------:|:--------:|:-----|
| Response    |  str   | "success" or InvalidURLException       |

