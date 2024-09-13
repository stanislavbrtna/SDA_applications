for pic in *.png; do
    convert "$pic" "${pic%.*}.ppm"
    ptp16 "${pic%.*}.ppm" "${pic%.*}.p16"
done

