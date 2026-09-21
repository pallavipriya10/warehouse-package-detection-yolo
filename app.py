import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import os


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Warehouse Package Detection",
    page_icon="📦",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("📦 Warehouse Package Detection & Counting")

st.markdown(
    """
    **Computer Vision Application using YOLO11**

    Upload a warehouse image to automatically detect and count packages.
    The trained deep learning model identifies packages and displays
    bounding boxes with confidence scores.
    """
)

st.divider()


# --------------------------------------------------
# LOAD TRAINED MODEL
# --------------------------------------------------
@st.cache_resource
def load_model():
    return YOLO("best.pt")


model = load_model()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.header("⚙️ Detection Settings")

confidence_threshold = st.sidebar.slider(
    "Confidence Threshold",
    min_value=0.10,
    max_value=0.90,
    value=0.40,
    step=0.05
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Model:** YOLO11n

    **Task:** Package Detection

    **Image Size:** 640 × 640

    **Classes:** 1 (Package)
    """
)


# --------------------------------------------------
# IMAGE UPLOAD
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "📤 Upload a Warehouse Image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    # --------------------------------------------------
    # ORIGINAL IMAGE
    # --------------------------------------------------
    st.subheader("🖼️ Uploaded Image")

    st.image(
        image,
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------
    # DETECTION BUTTON
    # --------------------------------------------------
    if st.button(
        "🔍 Detect Packages",
        type="primary",
        use_container_width=True
    ):

        with st.spinner("Running YOLO11 package detection..."):

            # Create temporary image
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".jpg"
            ) as temp_file:

                image.save(temp_file.name)
                image_path = temp_file.name

            # Run prediction
            results = model.predict(
                source=image_path,
                imgsz=640,
                conf=confidence_threshold,
                verbose=False
            )

            result = results[0]

            # Count packages
            package_count = len(result.boxes)

            # Generate annotated image
            annotated_image = result.plot()

            # Convert BGR → RGB
            annotated_image = annotated_image[:, :, ::-1]

            # Remove temporary file
            os.remove(image_path)

        # --------------------------------------------------
        # SUCCESS MESSAGE
        # --------------------------------------------------
        st.success("✅ Package detection completed successfully!")

        # --------------------------------------------------
        # METRICS
        # --------------------------------------------------
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "📦 Packages Detected",
                package_count
            )

        with col2:
            st.metric(
                "🎯 Confidence Threshold",
                f"{confidence_threshold:.0%}"
            )

        with col3:

            if package_count > 0:

                confidences = [
                    float(box.conf[0])
                    for box in result.boxes
                ]

                average_confidence = (
                    sum(confidences) / len(confidences)
                )

                st.metric(
                    "📊 Average Confidence",
                    f"{average_confidence:.2%}"
                )

            else:

                st.metric(
                    "📊 Average Confidence",
                    "N/A"
                )

        st.divider()

        # --------------------------------------------------
        # DETECTION RESULT
        # --------------------------------------------------
        st.subheader("🎯 Detection Results")

        st.image(
            annotated_image,
            caption="Detected Packages with Bounding Boxes",
            use_container_width=True
        )

        # --------------------------------------------------
        # DETECTION DETAILS
        # --------------------------------------------------
        st.subheader("📋 Detection Details")

        if package_count > 0:

            for i, box in enumerate(result.boxes):

                confidence = float(box.conf[0])

                st.write(
                    f"**Package {i + 1}** — "
                    f"Confidence: **{confidence:.2%}**"
                )

        else:

            st.warning(
                "⚠️ No packages detected. "
                "Try lowering the confidence threshold."
            )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()

st.caption(
    "Warehouse Package Detection & Counting | "
    "Computer Vision Project using YOLO11"
)