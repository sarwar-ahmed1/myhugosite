
variable "cohort" {
  description = "User cohort name"
  type        = string
}

variable "env" {
  description = "Environment where resource lies"
  type        = string
}

variable "user" {
  description = "User cloud ID"
  type        = string

}

variable "instance" {
  description = "Instance for the resource group"
  type        = number
}

variable "pod_tag" {
  description = "pod name"
  type        = string
}

variable "purpose" {
  description = "purpose"
  type        = string
}

variable "location" {
  type = string
}
