output "jenkins_public_ip" {
  description = "Use this IP to access Jenkins UI"
  value       = google_compute_instance.jenkins_vm.network_interface[0].access_config[0].nat_ip
}

output "repository_url" {
  description = "The Docker repository URL in Artifact Registry"
  value       = "${var.region}-docker.pkg.dev/${var.project_id}/${google_artifact_registry_repository.docker_repo.name}"
}