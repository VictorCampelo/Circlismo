import { ProcessImageForm } from "../../Molecules/ProcessImageForm";
import useErrorBoundary from "use-error-boundary";

import "./style.scss";
import { CardUploadedImage } from "../../Molecules/CardUploadedImage";
import { CardDonwloadedImage } from "../../Molecules/CardDownloadedImage";
import { CardNumberatedImage } from "../../Molecules/CardNumberatedImage";

export function Preview() {
  const { ErrorBoundary, didCatch, error } = useErrorBoundary();

  return (
    <>
      {didCatch ? (
        <p>An error has been caught: {error.message}</p>
      ) : (
        <ErrorBoundary>
          <div className="previewComponent">
            <ProcessImageForm />
          </div>
          <div className="previewImages">
            <CardUploadedImage text="Original Image" />
            <CardDonwloadedImage text="Circlism Image" />
            <CardNumberatedImage text="Numbered Circlism Image" />
          </div>
        </ErrorBoundary>
      )}
    </>
  );
}
