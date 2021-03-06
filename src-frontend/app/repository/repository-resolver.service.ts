import { Injectable } from '@angular/core';
import { Router, Resolve, ActivatedRouteSnapshot } from '@angular/router';

import { Repository } from './repository.model';
import { RepositoryService } from './repository.service';

@Injectable()
export class RepositoryResolver implements Resolve<Repository> {
    constructor(
        private repositoryService: RepositoryService,
        private router: Router
    ) {}

    resolve(route: ActivatedRouteSnapshot): Repository {
        // Ensure a repo with the specified info actually exists.
        // This check also ensures that this user has permissions to
        // this repo (since the backend does that).
        const repository = this.repositoryService.getByDisplayName(
            route.params['login'],
            route.params['name']
        )
        if (repository) {
            return repository;
        } else {
            this.router.navigate(['/repos']);
            return null;
        }
    }
}
