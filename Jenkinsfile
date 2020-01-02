node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("joebuhr/speedtestpy")
    }

    stage('Test image') {
        /* Ideally, we would run a test framework against our image.
         * For this example, we're using a Volkswagen-type approach ;-) */

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Scan image') {
        twistlockScan ca: '',
            cert: '',
            compliancePolicy: 'warn',
            containerized: false,
            dockerAddress: 'unix:///var/run/docker.sock',
            gracePeriodDays: 0,
            ignoreImageBuildTime: true,
            image: 'joebuhr/speedtestpy',
            key: '',
            logLevel: 'true',
            policy: 'warn',
            requirePackageUpdate: false,
            timeout: 10
}

    stage('Publish scan results') {
        twistlockPublish ca: '',
            cert: '',
            dockerAddress: 'unix:///var/run/docker.sock',
            image: 'joebuhr/speedtestpy',
            key: '',
            logLevel: 'true',
            timeout: 10
}

    stage('Push image') {
        /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. */
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}
