import torch
import argparse
import collections

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--input_model_path", type=str, default="pytorch_model.bin",
                    help=".")
parser.add_argument("--output_model_path", type=str, default="huggingface_model.bin",
                    help=".")
parser.add_argument("--layers_num", type=int, default=12, help=".")


args = parser.parse_args()
path = args.input_model_path

input_model = torch.load(args.input_model_path)

output_model = collections.OrderedDict()

output_model["model.shared.weight"] = input_model["embedding.word_embedding.weight"]
output_model["model.encoder.embed_positions.weight"] = input_model["embedding.pe"].squeeze(1)
output_model["model.decoder.embed_positions.weight"] = input_model["target.embedding.pe"].squeeze(1)
output_model["model.encoder.embed_tokens.weight"] = input_model["embedding.word_embedding.weight"]
output_model["model.decoder.embed_tokens.weight"] = input_model["embedding.word_embedding.weight"]
output_model["lm_head.weight"] = input_model["target.output_layer.weight"]
output_model["final_logits_bias"] = input_model["target.output_layer.bias"].unsqueeze(0)
for i in range(args.layers_num):
    output_model["model.encoder.layers." + str(i) + ".self_attn.q_proj.weight"] = input_model["encoder.transformer." + str(i) + ".self_attn.linear_layers.0.weight"]
    output_model["model.encoder.layers." + str(i) + ".self_attn.q_proj.bias"] = input_model["encoder.transformer." + str(i) + ".self_attn.linear_layers.0.bias"]
    output_model["model.encoder.layers." + str(i) + ".self_attn.k_proj.weight"] = input_model["encoder.transformer." + str(i) + ".self_attn.linear_layers.1.weight"]
    output_model["model.encoder.layers." + str(i) + ".self_attn.k_proj.bias"] = input_model["encoder.transformer." + str(i) + ".self_attn.linear_layers.1.bias"]
    output_model["model.encoder.layers." + str(i) + ".self_attn.v_proj.weight"] = input_model["encoder.transformer." + str(i) + ".self_attn.linear_layers.2.weight"]
    output_model["model.encoder.layers." + str(i) + ".self_attn.v_proj.bias"] = input_model["encoder.transformer." + str(i) + ".self_attn.linear_layers.2.bias"]
    output_model["model.encoder.layers." + str(i) + ".self_attn.out_proj.weight"] = input_model["encoder.transformer." + str(i) + ".self_attn.final_linear.weight"]
    output_model["model.encoder.layers." + str(i) + ".self_attn.out_proj.bias"] = input_model["encoder.transformer." + str(i) + ".self_attn.final_linear.bias"]
    output_model["model.encoder.layers." + str(i) + ".self_attn_layer_norm.weight"] = input_model["encoder.transformer." + str(i) + ".layer_norm_1.gamma"]
    output_model["model.encoder.layers." + str(i) + ".self_attn_layer_norm.bias"] = input_model["encoder.transformer." + str(i) + ".layer_norm_1.beta"]
    output_model["model.encoder.layers." + str(i) + ".fc1.weight"] = input_model["encoder.transformer." + str(i) + ".feed_forward.linear_1.weight"]
    output_model["model.encoder.layers." + str(i) + ".fc1.bias"] = input_model["encoder.transformer." + str(i) + ".feed_forward.linear_1.bias"]
    output_model["model.encoder.layers." + str(i) + ".fc2.weight"] = input_model["encoder.transformer." + str(i) + ".feed_forward.linear_2.weight"]
    output_model["model.encoder.layers." + str(i) + ".fc2.bias"] = input_model["encoder.transformer." + str(i) + ".feed_forward.linear_2.bias"]
    output_model["model.encoder.layers." + str(i) + ".final_layer_norm.weight"] = input_model["encoder.transformer." + str(i) + ".layer_norm_2.gamma"]
    output_model["model.encoder.layers." + str(i) + ".final_layer_norm.bias"] = input_model["encoder.transformer." + str(i) + ".layer_norm_2.beta"]

    output_model["model.decoder.layers." + str(i) + ".self_attn.q_proj.weight"] = input_model["target.decoder.transformer_decoder." + str(i) + ".self_attn.linear_layers.0.weight"]
    output_model["model.decoder.layers." + str(i) + ".self_attn.q_proj.bias"] = input_model["target.decoder.transformer_decoder." + str(i) + ".self_attn.linear_layers.0.bias"]
    output_model["model.decoder.layers." + str(i) + ".self_attn.k_proj.weight"] = input_model["target.decoder.transformer_decoder." + str(i) + ".self_attn.linear_layers.1.weight"]
    output_model["model.decoder.layers." + str(i) + ".self_attn.k_proj.bias"] = input_model["target.decoder.transformer_decoder." + str(i) + ".self_attn.linear_layers.1.bias"]
    output_model["model.decoder.layers." + str(i) + ".self_attn.v_proj.weight"] = input_model["target.decoder.transformer_decoder." + str(i) + ".self_attn.linear_layers.2.weight"]
    output_model["model.decoder.layers." + str(i) + ".self_attn.v_proj.bias"] = input_model["target.decoder.transformer_decoder." + str(i) + ".self_attn.linear_layers.2.bias"]
    output_model["model.decoder.layers." + str(i) + ".self_attn.out_proj.weight"] = input_model["target.decoder.transformer_decoder." + str(i) + ".self_attn.final_linear.weight"]
    output_model["model.decoder.layers." + str(i) + ".self_attn.out_proj.bias"] = input_model["target.decoder.transformer_decoder." + str(i) + ".self_attn.final_linear.bias"]
    output_model["model.decoder.layers." + str(i) + ".self_attn_layer_norm.weight"] = input_model["target.decoder.transformer_decoder." + str(i) + ".layer_norm_1.gamma"]
    output_model["model.decoder.layers." + str(i) + ".self_attn_layer_norm.bias"] = input_model["target.decoder.transformer_decoder." + str(i) + ".layer_norm_1.beta"]

    output_model["model.decoder.layers." + str(i) + ".encoder_attn.q_proj.weight"] = input_model["target.decoder.transformer_decoder." + str(i) + ".context_attn.linear_layers.0.weight"]
    output_model["model.decoder.layers." + str(i) + ".encoder_attn.q_proj.bias"] = input_model["target.decoder.transformer_decoder." + str(i) + ".context_attn.linear_layers.0.bias"]
    output_model["model.decoder.layers." + str(i) + ".encoder_attn.k_proj.weight"] = input_model["target.decoder.transformer_decoder." + str(i) + ".context_attn.linear_layers.1.weight"]
    output_model["model.decoder.layers." + str(i) + ".encoder_attn.k_proj.bias"] = input_model["target.decoder.transformer_decoder." + str(i) + ".context_attn.linear_layers.1.bias"]
    output_model["model.decoder.layers." + str(i) + ".encoder_attn.v_proj.weight"] = input_model["target.decoder.transformer_decoder." + str(i) + ".context_attn.linear_layers.2.weight"]
    output_model["model.decoder.layers." + str(i) + ".encoder_attn.v_proj.bias"] = input_model["target.decoder.transformer_decoder." + str(i) + ".context_attn.linear_layers.2.bias"]
    output_model["model.decoder.layers." + str(i) + ".encoder_attn.out_proj.weight"] = input_model["target.decoder.transformer_decoder." + str(i) + ".context_attn.final_linear.weight"]
    output_model["model.decoder.layers." + str(i) + ".encoder_attn.out_proj.bias"] = input_model["target.decoder.transformer_decoder." + str(i) + ".context_attn.final_linear.bias"]
    output_model["model.decoder.layers." + str(i) + ".encoder_attn_layer_norm.weight"] = input_model["target.decoder.transformer_decoder." + str(i) + ".layer_norm_2.gamma"]
    output_model["model.decoder.layers." + str(i) + ".encoder_attn_layer_norm.bias"] = input_model["target.decoder.transformer_decoder." + str(i) + ".layer_norm_2.beta"]

    output_model["model.decoder.layers." + str(i) + ".fc1.weight"] = input_model["target.decoder.transformer_decoder." + str(i) + ".feed_forward.linear_1.weight"]
    output_model["model.decoder.layers." + str(i) + ".fc1.bias"] = input_model["target.decoder.transformer_decoder." + str(i) + ".feed_forward.linear_1.bias"]
    output_model["model.decoder.layers." + str(i) + ".fc2.weight"] = input_model["target.decoder.transformer_decoder." + str(i) + ".feed_forward.linear_2.weight"]
    output_model["model.decoder.layers." + str(i) + ".fc2.bias"] = input_model["target.decoder.transformer_decoder." + str(i) + ".feed_forward.linear_2.bias"]
    output_model["model.decoder.layers." + str(i) + ".final_layer_norm.weight"] = input_model["target.decoder.transformer_decoder." + str(i) + ".layer_norm_3.gamma"]
    output_model["model.decoder.layers." + str(i) + ".final_layer_norm.bias"] = input_model["target.decoder.transformer_decoder." + str(i) + ".layer_norm_3.beta"]


output_model["model.encoder.layer_norm.weight"] = input_model["encoder.layer_norm.gamma"]
output_model["model.encoder.layer_norm.bias"] = input_model["encoder.layer_norm.beta"]
output_model["model.decoder.layer_norm.weight"] = input_model["target.decoder.layer_norm.gamma"]
output_model["model.decoder.layer_norm.bias"] = input_model["target.decoder.layer_norm.beta"]

torch.save(output_model, args.output_model_path)