from ultralytics import YOLO
from ultralytics.data.converter import convert_coco
from roboflow import Roboflow


def get_data():
    rf = Roboflow(api_key="rwvQ9T2ZAUYSklSEtdqZ")
    project = rf.workspace("tennis-ai").project("football-boxes")
    version = project.version(1)
    dataset = version.download("coco-segmentation")

    # Convert to YOLO format
    
    return dataset


def train():

    model: YOLO = YOLO('yolov8s-seg.pt')  # load a pretrained model (recommended for training)
    # model = YOLO('yolov8n-seg.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

    # Train the model
    results = model.train(data=f'C:\\Users\\7kevi\\Documents\\GitHub\\FutbolPassing\\video_work\\dataset.yaml', epochs=10, imgsz=640)
    return results, model


if __name__ == '__main__':

    #### THIS SECTION IS ONLY TO GET THE DATA SET.
    download_the_data = False
    if download_the_data:
        data = get_data() # This will give you the data into a folder called football-boxes-1
        convert_coco('football-boxes-1/test' ,use_segments=True, save_dir='./data/test')
        convert_coco('football-boxes-1/train', use_segments=True, save_dir='./data/train')
        convert_coco('football-boxes-1/valid', use_segments=True, save_dir='./data/valid')
        # following this section, you have to move the data into the correct folders:
            # + data
            #   + train
            #       + images (all jpeg files)
            #       + labels (make sure this is all txt files)
            #   + test
            #       + images 
            #       + labels
            #   + valid
            #       + images
            #       + labels
        exit()

    model = train()

