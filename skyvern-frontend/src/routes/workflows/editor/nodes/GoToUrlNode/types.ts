import type { Node } from "@xyflow/react";
import { NodeBaseData } from "../types";

export type GoToUrlNodeData = NodeBaseData & {
  url: string;
  errorCodeMapping: string;
  maxRetries: number | null;
  maxStepsOverride: number | null;
  allowDownloads: boolean;
  downloadSuffix: string | null;
  parameterKeys: Array<string>;
  totpVerificationUrl: string | null;
  totpIdentifier: string | null;
  cacheActions: boolean;
};

export type GoToUrlNode = Node<GoToUrlNodeData, "goToUrl">;

export const goToUrlNodeDefaultData: GoToUrlNodeData = {
  label: "",
  url: "",
  errorCodeMapping: "null",
  maxRetries: null,
  maxStepsOverride: null,
  allowDownloads: false,
  downloadSuffix: null,
  editable: true,
  parameterKeys: [],
  totpVerificationUrl: null,
  totpIdentifier: null,
  continueOnFailure: false,
  cacheActions: false,
} as const;

export function isGoToUrlNode(node: Node): node is GoToUrlNode {
  return node.type === "goToUrl";
}
