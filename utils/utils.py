from models.basenet import *
import torch
import os


def get_model_mme(net, num_class=13, unit_size=2048, temp=0.05):
    model_g = ResBase(net, unit_size=unit_size)
    model_c = ResClassifier_MME(num_classes=num_class,
                                input_size=unit_size,
                                temp=temp)
    return model_g, model_c


def save_model(model_g, model_c, save_path):
    save_dic = {
        'g_state_dict': model_g.state_dict(),
        'c_state_dict': model_c.state_dict(),
    }
    torch.save(save_dic, save_path)


def load_model(model_g, model_c, load_path):
    checkpoint = torch.load(load_path)
    model_g.load_state_dict(checkpoint['g_state_dict'])
    model_c.load_state_dict(checkpoint['c_state_dict'])
    return model_g, model_c


def log_set(kwargs):
    source_data = kwargs["source_data"]
    target_data = kwargs["target_data"]
    seed = kwargs["seed"]

    target_data = os.path.splitext(os.path.basename(target_data))[0]

    logname = "log.txt"
    logname = os.path.join(kwargs["output_dir"], logname)
    if not os.path.exists(os.path.dirname(logname)):
        os.makedirs(os.path.dirname(logname))
    print("record in %s " % logname)
    import logging
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=logname, format="%(message)s")
    logger.setLevel(logging.INFO)
    logger.info("{}_2_{}".format(source_data, target_data))
    logger.info("use random seed:{}".format(seed))
    return logname
