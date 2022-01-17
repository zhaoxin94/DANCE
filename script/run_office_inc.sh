#!/bin/sh
python $2 --config configs/office-train-config_CLDA.yaml --exp_name $3 --source /home/grad3/keisaito/domain_adaptation/CRAWL/txt/source_amazon_obda_few_v2.txt --target_u /home/grad3/keisaito/domain_adaptation/CRAWL/txt/target_dslr_obda_few_v2.txt --target_l /home/grad3/keisaito/domain_adaptation/CRAWL/txt/target_dslr_obda_few_label_v2.txt --gpu_device $1
python $2 --config configs/office-train-config_CLDA.yaml --exp_name $3 --source /home/grad3/keisaito/domain_adaptation/CRAWL/txt/source_amazon_obda_few_v2.txt --target_u /home/grad3/keisaito/domain_adaptation/CRAWL/txt/target_webcam_obda_few_v2.txt --target_l /home/grad3/keisaito/domain_adaptation/CRAWL/txt/target_webcam_obda_few_label_v2.txt --gpu_device $1
python $2 --config configs/office-train-config_CLDA.yaml --exp_name $3 --source /home/grad3/keisaito/domain_adaptation/CRAWL/txt/source_webcam_obda_few_v2.txt --target_u /home/grad3/keisaito/domain_adaptation/CRAWL/txt/target_dslr_obda_few_v2.txt --target_l /home/grad3/keisaito/domain_adaptation/CRAWL/txt/target_dslr_obda_few_label_v2.txt --gpu_device $1
python $2 --config configs/office-train-config_CLDA.yaml --exp_name $3 --source /home/grad3/keisaito/domain_adaptation/CRAWL/txt/source_webcam_obda_few_v2.txt --target_u /home/grad3/keisaito/domain_adaptation/CRAWL/txt/target_amazon_obda_few_v2.txt --target_l /home/grad3/keisaito/domain_adaptation/CRAWL/txt/target_amazon_obda_few_label_v2.txt --gpu_device $1
python $2 --config configs/office-train-config_CLDA.yaml --exp_name $3 --source /home/grad3/keisaito/domain_adaptation/CRAWL/txt/source_dslr_obda_few_v2.txt --target_u /home/grad3/keisaito/domain_adaptation/CRAWL/txt/target_amazon_obda_few_v2.txt --target_l /home/grad3/keisaito/domain_adaptation/CRAWL/txt/target_amazon_obda_few_label_v2.txt --gpu_device $1
python $2 --config configs/office-train-config_CLDA.yaml --exp_name $3 --source /home/grad3/keisaito/domain_adaptation/CRAWL/txt/source_dslr_obda_few_v2.txt --target_u /home/grad3/keisaito/domain_adaptation/CRAWL/txt/target_webcam_obda_few_v2.txt --target_l /home/grad3/keisaito/domain_adaptation/CRAWL/txt/target_webcam_obda_few_label_v2.txt --gpu_device $1
