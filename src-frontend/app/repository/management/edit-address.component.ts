import { Component, OnInit, EventEmitter, Input, Output } from '@angular/core';

import { Repository } from '../repository.model';
import { RepositoryService } from '../repository.service';

@Component({
    selector: 'edit-address',
    templateUrl: './edit-address.component.html',
})
export class EditAddressComponent implements OnInit {
    @Input() repository: Repository;
    @Output() editCanceled = new EventEmitter();
    @Output() editSaved = new EventEmitter();
    errorMessage: string;
    newAddress: string;
    saving = false;

    constructor(
        private repositoryService: RepositoryService,
    ) {}

    ngOnInit() {
        this.newAddress = this.repository.email_slug;
        this.errorMessage = '';
    }

    cancel() {
        this.editCanceled.emit();
    }

    save() {
        this.saving = true;
        this.errorMessage = '';
        this.repositoryService.updateAddress(this.repository, this.newAddress)
            .then((updatedRepository) => this.editSaved.emit(updatedRepository))
            .catch((errorMessage: string) => {
                this.errorMessage = errorMessage;
                this.saving = false;
            });
    }
}
