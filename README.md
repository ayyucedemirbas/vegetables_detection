# vegetables_detection


You can download the dataset from Kaggle: https://www.kaggle.com/datasets/ayyuce/vegetables?datasetId=2036840


![0](https://user-images.githubusercontent.com/8023150/160719971-79a94626-cef8-4e7b-9b07-7bfb84181bf6.png)


<img width="960" alt="image" src="https://user-images.githubusercontent.com/8023150/160720076-1649d419-6428-48f4-a81f-c477a44b6c43.png">

![20](https://user-images.githubusercontent.com/8023150/160720106-9bb3ff0c-ad59-4e0c-b964-c9a7bdea3fcb.png)

## The Model


                         from  n    params  module                                  arguments                     
          0                -1  1      3520  models.common.Conv                      [3, 32, 6, 2, 2]              
          1                -1  1     18560  models.common.Conv                      [32, 64, 3, 2]                
          2                -1  1     18816  models.common.C3                        [64, 64, 1]                   
          3                -1  1     73984  models.common.Conv                      [64, 128, 3, 2]               
          4                -1  2    115712  models.common.C3                        [128, 128, 2]                 
          5                -1  1    295424  models.common.Conv                      [128, 256, 3, 2]              
          6                -1  3    625152  models.common.C3                        [256, 256, 3]                 
          7                -1  1   1180672  models.common.Conv                      [256, 512, 3, 2]              
          8                -1  1   1182720  models.common.C3                        [512, 512, 1]                 
          9                -1  1    656896  models.common.SPPF                      [512, 512, 5]                 
         10                -1  1    131584  models.common.Conv                      [512, 256, 1, 1]              
         11                -1  1         0  torch.nn.modules.upsampling.Upsample    [None, 2, 'nearest']          
         12           [-1, 6]  1         0  models.common.Concat                    [1]                           
         13                -1  1    361984  models.common.C3                        [512, 256, 1, False]          
         14                -1  1     33024  models.common.Conv                      [256, 128, 1, 1]              
         15                -1  1         0  torch.nn.modules.upsampling.Upsample    [None, 2, 'nearest']          
         16           [-1, 4]  1         0  models.common.Concat                    [1]                           
         17                -1  1     90880  models.common.C3                        [256, 128, 1, False]          
         18                -1  1    147712  models.common.Conv                      [128, 128, 3, 2]              
         19          [-1, 14]  1         0  models.common.Concat                    [1]                           
         20                -1  1    296448  models.common.C3                        [256, 256, 1, False]          
         21                -1  1    590336  models.common.Conv                      [256, 256, 3, 2]              
         22          [-1, 10]  1         0  models.common.Concat                    [1]                           
         23                -1  1   1182720  models.common.C3                        [512, 512, 1, False]          
         24      [17, 20, 23]  1     32364  models.yolo.Detect                      [7, [[10, 13, 16, 30, 33, 23], [30, 61, 62, 45, 59, 119], [116, 90, 156, 198, 373, 326]], [128, 256, 512]]
        Model summary: 270 layers, 7038508 parameters, 7038508 gradients, 15.9 GFLOPs
        
        
  ## Hyperparameters for COCO training from scratch
        # python train.py --batch 40 --cfg yolov5m.yaml --weights '' --data coco.yaml --img 640 --epochs 300
        # See tutorials for hyperparameter evolution https://github.com/ultralytics/yolov5#tutorials


        lr0: 0.01  # initial learning rate (SGD=1E-2, Adam=1E-3)
        lrf: 0.2  # final OneCycleLR learning rate (lr0 * lrf)
        momentum: 0.937  # SGD momentum/Adam beta1
        weight_decay: 0.0005  # optimizer weight decay 5e-4
        warmup_epochs: 3.0  # warmup epochs (fractions ok)
        warmup_momentum: 0.8  # warmup initial momentum
        warmup_bias_lr: 0.1  # warmup initial bias lr
        box: 0.05  # box loss gain
        cls: 0.5  # cls loss gain
        cls_pw: 1.0  # cls BCELoss positive_weight
        obj: 1.0  # obj loss gain (scale with pixels)
        obj_pw: 1.0  # obj BCELoss positive_weight
        iou_t: 0.20  # IoU training threshold
        anchor_t: 4.0  # anchor-multiple threshold
        # anchors: 3  # anchors per output layer (0 to ignore)
        fl_gamma: 0.0  # focal loss gamma (efficientDet default gamma=1.5)
        hsv_h: 0.015  # image HSV-Hue augmentation (fraction)
        hsv_s: 0.7  # image HSV-Saturation augmentation (fraction)
        hsv_v: 0.4  # image HSV-Value augmentation (fraction)
        degrees: 0.0  # image rotation (+/- deg)
        translate: 0.1  # image translation (+/- fraction)
        scale: 0.5  # image scale (+/- gain)
        shear: 0.0  # image shear (+/- deg)
        perspective: 0.0  # image perspective (+/- fraction), range 0-0.001
        flipud: 0.0  # image flip up-down (probability)
        fliplr: 0.5  # image flip left-right (probability)
        mosaic: 1.0  # image mosaic (probability)
        mixup: 0.0  # image mixup (probability)


<img width="656" alt="image" src="https://user-images.githubusercontent.com/8023150/160721230-92f43074-77b0-454b-a59e-606cf32629ab.png">

<img width="501" alt="image" src="https://user-images.githubusercontent.com/8023150/160721257-25334adb-e959-458b-8311-4a4152b75736.png">

<img width="530" alt="image" src="https://user-images.githubusercontent.com/8023150/160721735-3d23d943-3cdd-4751-b360-8a86e344c9f3.png">



