import { ProcessImageForm } from "../../Molecules/ProcessImageForm";
import { ImageUploaded } from "../../Atoms/ImageUploaded";
import { ImageDownloaded } from "../../Atoms/ImageDownloaded";
import useErrorBoundary from "use-error-boundary";

import "./style.scss";

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
            <ImageUploaded />
            <ImageDownloaded />
            <ImageDownloaded />
          </div>
        </ErrorBoundary>
      )}
    </>
  );
}
