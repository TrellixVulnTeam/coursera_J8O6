from collections import namedtuple
import config
import numpy as np
import tensorflow as tf

Batch = namedtuple("Batch", [
    # Fake
    "fake_class_label",
    "fake_z",
    "fake_x",
    # Real
    "real_class_label",
    "real_x",
    # Combined
    "combined_x",
    "combined_class_label",
    "combined_authenticity_label",
])

def generate_z(num_samples):
    # TODO: Appears to be very important that this is uniform!!
    return np.random.uniform(
        low = -1,
        high = +1,
        size = [num_samples, config.Z_DIMS]
    )

def generate_x(run_info, num_samples, fake_class_label, z):
    session, graph = run_info.session, run_info.graph
    return session.run(graph.generator.generated_x, feed_dict = {
        graph.generator.class_label: fake_class_label,
        graph.generator.z: z,
    })

def generate_fake_data(run_info, num_classes, num_samples):
    fake_class_label = np.random.choice(
        num_classes, size = num_samples, replace = True
    )
    fake_z = generate_z(num_samples)
    fake_x = generate_x(
        run_info = run_info,
        num_samples = num_samples,
        fake_class_label = fake_class_label,
        z = fake_z
    )

    return (fake_class_label, fake_z, fake_x)

def select_real_data(dataset, num_samples):
    real_x, real_class_label = dataset.next_batch(num_samples)

    # Reshape and renormalize to (-1, +1)
    real_x = real_x.reshape([-1, config.IMAGE_DIMS])
    real_x = (2 * real_x) - 1

    return (real_class_label, real_x)

def next_batch(run_info, batch_size):
    fake_class_label, fake_z, fake_x = generate_fake_data(
        run_info,
        num_classes = config.NUM_CLASSES,
        num_samples = batch_size,
    )
    real_class_label, real_x = select_real_data(
        dataset = run_info.dataset,
        num_samples = batch_size,
    )

    # Concatenate real and fake results
    combined_x = np.concatenate([real_x, fake_x], axis = 0)
    combined_class_label = np.concatenate(
        [real_class_label, fake_class_label], axis = 0
    )
    combined_authenticity_label = np.concatenate(
        [np.ones(batch_size), np.zeros(batch_size)],
        axis = 0
    )

    return Batch(
        fake_class_label = fake_class_label,
        fake_z = fake_z,
        fake_x = fake_x,

        real_class_label = real_class_label,
        real_x = real_x,

        combined_x = combined_x,
        combined_class_label = combined_class_label,
        combined_authenticity_label = combined_authenticity_label
    )
